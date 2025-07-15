## Task Localization

TAPS and PsyFlow make cross-cultural localization efficient by cleanly separating task logic from configuration and content. This modular design allows researchers to adapt paradigms across languages and cultural contexts **without modifying the task code**, promoting global accessibility, reproducibility, and reuse.

**Why It Matters**: Localization is essential for making psychological tasks globally accessible and inclusive. By adapting tasks to different languages and cultural contexts, researchers can extend their reach, maintain standardization across implementations, ensure reproducibility of results, and improve usability for diverse participant groups—including children, older adults, and individuals with limited literacy.


**How It Works** In a TAPS-compliant task, all participant-facing content is cleanly separated from the task logic and stored in the `config.yaml` file. Specifically, localization targets the `subinfo_mapping` section (for registration labels and messages) and the `stimuli` section (for all `text` or `textbox` content). This modular structure enables full language adaptation without modifying any core Python code.


### 1. Manual Adaptation (Quick and Easy)

The simplest way to localize your task is to **manually translate** the `config/config.yaml` file. This is ideal when you're using LLMs interactively (e.g., ChatGPT, Gemini, DeepSeek, Claude).

Paste your YAML content directly into an LLM chat window, along with a clear instruction. 

**Here's an example prompt:**
```{Prompt}
Translate the following YAML fields into Japanese.
1. The right-hand values of subinfo_mapping (e.g., messages, instructional text).
2. The text content of stimuls of text and textbox
3. Do not modify YAML structure, indentation, or key names.
4. Preserve placeholder variables such as {field}, {duration}, {block_num} exactly as they are.
5. For multiline text fields, preserve line breaks and do not introduce extra quotation marks or escape characters.
6. Do not include any commentary, markdown, or explanation—output the translated YAML only.
7. Output the full yaml content in a code block
Here is the original yaml content:
```
**Orignal config.yaml**

To save space we just show the relevant content.
```{yaml}
# config.yaml
# === Subject info ===
subinfo_mapping:
    subject_id: "被试号"
    subname: "被试姓名(拼音)"
    age: "年龄"
    gender: "性别"
    Male: "男"
    Female: "女"
    registration_failed: "注册失败。"
    registration_successful: "注册成功！"
    invalid_input: "字段 {field} 输入无效"

# === Stimuli (for SST task) ===
stimuli:
  fixation:
    type: text
    text: "+"
    color: white

  no_response_feedback  :
    type: text
    text: |
      【未按键】
      请在箭头出现后按键
    font: SimHei
    height: 0.78

  block_break:
    type: text
    text: |
      【休息提示】

      第 {block_num} / {total_blocks} 部分完成。
      击中率：{go_accuracy:.2f}
      正确停止率：{stop_accuracy:.2f}

      请在充分休息后按【空格键】
      进入下一部分
    color: white
    font: SimHei
    height: 0.78


  instruction_text:
    type: textbox
    text: |
      【停止信号任务说明】

      在本任务中，您将看到箭头指向左或右
      您的目标是尽快且准确地做出反应
        - 如果箭头指向左，请用左手食指按【F】
        - 如果箭头指向右，请用右手食指按【J】

      注意：在某些试次中
      箭头出现后不久会出现红色箭头
      当看到红色箭头时
      请尽力抑制您的反应不要按任何按键

      在没有红色箭头出现时，请快速做出反应
      出现红色箭头时，请尽量不做出任何按键反应

      准备好后，请按【空格键】开始任务。
    color: white
    font: SimHei
    alignment: center
    letterHeight: 0.78
    units: deg
    size: [20, 5]

  iti_stim:
    type: text
    text: ""

  good_bye:
    type: textbox
    text: |
      任务结束
      
      感谢您的参与
      请按【空格键】键退出
    color: white
    font: SimHei
    alignment: center
    letterHeight: 0.78

```
Then copy the translated YAML back into your project and save as a localized config file, e.g., `config.ja.yaml`.

**Translated config.ja.yaml** 

To save space we just show the relevant content.
```{yaml}
# config.yaml
# === Subject info ===
subinfo_mapping:
    subject_id: "被験者ID"
    subname: "被験者氏名（ローマ字）"
    age: "年齢"
    gender: "性別"
    Male: "男性"
    Female: "女性"
    registration_failed: "登録に失敗しました。"
    registration_successful: "登録に成功しました！"
    invalid_input: "フィールド {field} の入力が無効です"

# === Stimuli (for SST task) ===
stimuli:
  fixation:
    type: text
    text: "+"
    color: white

  no_response_feedback  :
    type: text
    text: |
      【未反応】
      矢印が表示されたらキーを押してください
    font: SimHei
    height: 0.78

  block_break:
    type: text
    text: |
      【休憩のお知らせ】

      第 {block_num} / {total_blocks} ブロックが完了しました。
      命中率：{go_accuracy:.2f}
      正しく停止できた割合：{stop_accuracy:.2f}

      十分に休憩した後、【スペースキー】を押して
      次のブロックに進んでください
    color: white
    font: SimHei
    height: 0.78

  instruction_text:
    type: textbox
    text: |
      【ストップシグナル課題の説明】

      この課題では、矢印が左または右を指します。
      できるだけ素早く正確に反応してください。
        - 矢印が左を指したら、左手の人差し指で【F】を押してください。
        - 矢印が右を指したら、右手の人差し指で【J】を押してください。

      注意：一部の試行では、
      矢印の直後に赤い矢印が表示されることがあります。
      赤い矢印が表示されたら、
      反応を抑えてキーを押さないようにしてください。

      赤い矢印が表示されなければ、すぐに反応してください。
      赤い矢印が表示された場合は、できるだけ反応しないでください。

      準備ができたら【スペースキー】を押して課題を開始してください。
    color: white
    font: SimHei
    alignment: center
    letterHeight: 0.78
    units: deg
    size: [20, 5]

  iti_stim:
    type: text
    text: ""

  good_bye:
    type: textbox
    text: |
      課題終了
      
      ご参加ありがとうございました
      【スペースキー】を押して終了してください
    color: white
    font: SimHei
    alignment: center
    letterHeight: 0.78
```

### 2. Programmatic Localization via API

For automated localization workflows, use the built-in `LLMClient` class. It supports Google Gemini and DeepSeek (OpenAI-compatible) providers.

It will translate:
- `subinfo_mapping` labels  
- Any `stimuli` with type `text` or `textbox`  

```python
from psyflow.llm import LLMClient
client = LLMClient(provider="gemini", api_key="your-key", model="gemini-1.5-flash")
translated_config = client.translate_config(
    target_language="Japanese"
)
# This translates in-memory without saving to disk.
```
More details can be found in {doc}`LLMs <LLMs>`.

### 3. Important Notes on Task Localization

1. **Always review the auto-translated content.** While LLM-based translation performs well in most cases, it's strongly recommended to have a native speaker verify the accuracy and cultural appropriateness of the translated text.

2. **Leverage text-to-speech (TTS) for multilingual audio delivery.**  
   Since `psyflow` supports TTS conversion, you can automatically generate audio files from the translated text. This enables consistent and scalable voice presentation across languages—without requiring human recordings.  


   If you plan to use voice content:
   1. Delete the original voice files in the `assets/` folder.
   2. Regenerate the audio using a TTS voice that matches the target language.

    See {doc}`Text-to-Voice <text2voice>` for details on how to configure voices and view the list of supported options.

