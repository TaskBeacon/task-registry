## 📦 BlockUnit: Managing Experimental Blocks

The `BlockUnit` class provides a flexible and structured way to manage a sequence of trials in an experiment. It supports condition generation, result tracking, hooks for block lifecycle, and summarization — all useful for building robust experimental pipelines in PsychoPy.

### 🧵 Summary of Key Methods
| Purpose                             | Method                               |
|-------------------------------------|--------------------------------------|
| Initialize block                    | `BlockUnit(block_id, block_idx, ...)` |
| Generate trial conditions           | `.generate_conditions(func, labels)` |
| Manually assign trials              | `.add_trials(trial_list)`            |
| Register hook before block starts   | `.on_start(func)`                    |
| Register hook after block ends      | `.on_end(func)`                      |
| Run all trials                      | `.run_trial(run_func, **kwargs)`     |
| Get trial-level results             | `.to_dict()`                         |
| Append results to external list     | `.to_dict(target_list)`              |
| Summarize block results             | `.summarize()` or `.summarize(func)` |
| Get number of trials                | `len(block)`                         |
| Log block info to console/log       | `.logging_block_info()`              |

### 1. Initialization

To use `BlockUnit`, you need to create an instance by passing basic information about the block, the experiment settings, and optionally, PsychoPy window and keyboard handlers.

Example:
```python
from your_package import BlockUnit

block = BlockUnit(
    block_id="block_01",
    block_idx=0,
    settings=settings,   # must have .trials_per_block and .block_seed
    window=win,
    keyboard=kb
)
```
- `block_id`: Unique identifier string.
- `block_idx`: Index of this block in the experiment.
- `settings`: A configuration object, typically with fields like `trials_per_block`, `block_seed`, and possibly `conditions`.
- `win`, `kb`: PsychoPy window and keyboard objects (optional but needed for actual trial running).


### 2. Generating Trial Conditions

You can generate trial conditions using a custom function. This enables dynamic and reproducible condition assignment.
```python
def generate_balanced_conditions(n, labels, seed=None):
    import numpy as np
    rng = np.random.default_rng(seed)
    reps = int(np.ceil(n / len(labels)))
    choices = rng.permutation(labels * reps)[:n]
    return np.array(choices)

block.generate_conditions(
    func=generate_balanced_conditions,
    condition_labels=["win", "lose", "neutral"]
)
```
This will populate `block.trials` with randomized trial conditions, e.g., `["win", "neutral", "lose", ...]`.

You can also assign trials manually:

```python
block.add_trials(["win", "win", "neutral", "lose", "lose"])
```


### 3. Registering Block Hooks

You can register functions to be called automatically **before** and **after** the block runs, useful for setup and cleanup steps like logging, showing instructions, or saving snapshots.

Using decorator style:
```python
@block.on_start()
def on_block_start(b):
    print(f"Block {b.block_id} started.")

@block.on_end()
def on_block_end(b):
    print(f"Block {b.block_id} finished in {b.meta['duration']:.2f}s.")
```
Or functional style:
```python
block.on_start(lambda b: print("Prepare..."))
block.on_end(lambda b: print("Done."))
```


### 4. Running the Trials

To run the trials, you must provide a **trial function** that defines what happens on each trial. This function is called for each condition in `block.trials`. The **trial function** should be defined in a way that it accepts the block's window, keyboard, settings, and condition as parameters. It defines the flow of the trial, including stimulus presentation and response collection.

Trial function example:

```python
def run_trial(win, kb, settings, condition, **kwargs):
    print(f"Running condition: {condition}")
    # You'd show a stimulus here, wait for response, etc.
    return {
        "target_hit": 1 if condition == "win" else 0,
        "target_rt": 0.45
    }
```

Running the trial loop:

```python
block.run_trial(run_trial)
```
Each trial result is stored in `block.results`, enriched with trial index, block ID, and condition.


### 5. Summarizing Results

After a block has finished running, you can summarize results:

```python
summary = block.summarize()
```

Default summary includes:

- `hit_rate`: Average of `target_hit` across trials
- `avg_rt`: Mean `target_rt` (excluding None)

Example output:

```
    {
        "win": {"hit_rate": 1.0, "avg_rt": 0.42},
        "neutral": {"hit_rate": 0.5, "avg_rt": 0.51},
        "lose": {"hit_rate": 0.0, "avg_rt": 0.63}
    }
```

You can also pass a custom summarization function:

```python
def my_summary_func(block):
    return {"total_points": sum(r.get("score", 0) for r in block.results)}

block.summarize(my_summary_func)
```


### 6. Saving and Exporting Results

To convert the results into a list of dictionaries (e.g., for CSV export):

```python
results = block.to_dict()
```

To append results into an external list:

```python
all_results = []
block.to_dict(all_results)
```

### 7. Putting It All Together

Full example:

```python
block = BlockUnit("block1", 0, settings, window=win, keyboard=kb)

block.generate_conditions(generate_balanced_conditions, condition_labels=["reward", "punish"])

@block.on_start()
def show_instructions(b):
    print(f"Instructions for {b.block_id}")

def trial_func(win, kb, settings, cond):
    return {"target_hit": cond == "reward", "target_rt": 0.5}

block.run_trial(trial_func)

summary = block.summarize()
print(summary)
```

### 8. Realistic examples
#### 8.1. Monetary Incentive Delay Task (MID) example.

Note that we defined stim_bank and controller before the block loop, so they are available in the trial function across blocks. That means the dynamic controller is shared across blocks. If we want to have a different controller for each block, we should set it within the block loop.

```python
all_data = []
for block_i in range(settings.total_blocks):
    # setup block
    block = BlockUnit(
        block_id=f"block_{block_i}",
        block_idx=block_i,
        settings=settings,
        window=win,
        keyboard=keyboard
    )

    block.generate_conditions(func=generate_balanced_conditions)

    @block.on_start
    def _block_start(b):
        print("Block start {}".format(b.block_idx))
        # b.logging_block_info()
        trigger_sender.send(trigger_bank.get("block_onset"))
    @block.on_end
    def _block_end(b):     
        print("Block end {}".format(b.block_idx))
        trigger_sender.send(trigger_bank.get("block_end"))
        print(b.summarize())
        # print(b.describe())
    
    # run block
    block.run_trial(
        partial(run_trial, stim_bank=stim_bank, controller=controller, trigger_sender=trigger_sender, trigger_bank=trigger_bank)
    )
    
    block.to_dict(all_data)
    if block_i < settings.total_blocks - 1:
        StimUnit('block', win, kb).add_stim(stim_bank.get('block_break')).wait_and_continue()
    else:
        StimUnit('block', win, kb).add_stim(stim_bank.get_and_format('good_bye', reward=100)).wait_and_continue(terminate=True)
    
# Save all data to CSV
df = pd.DataFrame(all_data)
df.to_csv(settings.res_file, index=False)
```

#### 8.2. Probabilistic reversal learning (PRL) task example.

Note that we defined stim_bank within the block loop, so it is different for each block.

```python
all_data = []
for block_i in range(settings.total_blocks):
    stim_bank=StimBank(win)
    stima_img, stimb_img = pairs[block_i]
    cfg = stim_config.copy()
    cfg['stima']['image'] = stima_img
    cfg['stimb']['image'] = stimb_img
    stim_bank.add_from_dict(cfg)
    stim_bank.preload_all()

    controller = Controller.from_dict(controller_config)
    # setup block
    block = BlockUnit(
        block_id=f"block_{block_i}",
        block_idx=block_i,
        settings=settings,
        window=win,
        keyboard=keyboard
    )

    block.generate_conditions(func=generate_balanced_conditions)

    @block.on_start
    def _block_start(b):
        print("Block start {}".format(b.block_idx))
        # b.logging_block_info()
        triggersender.send(triggerbank.get("block_onset"))
    @block.on_end
    def _block_end(b):     
        print("Block end {}".format(b.block_idx))
        triggersender.send(triggerbank.get("block_end"))
        print(b.summarize())
        # print(b.describe())
    
    # run block
    block.run_trial(
        partial(run_trial, stim_bank=stim_bank, controller=controller,trigger_sender=triggersender, trigger_bank=triggerbank))
    
    block.to_dict(all_data)
    if block_i < settings.total_blocks - 1:
        StimUnit('block', win, kb).add_stim(stim_bank.get('block_break')).wait_and_continue()
    else:
        StimUnit('block', win, kb).add_stim(stim_bank.get('good_bye')).wait_and_continue(terminate=True)
    
df = pd.DataFrame(all_data)
df.to_csv(settings.res_file, index=False)
```