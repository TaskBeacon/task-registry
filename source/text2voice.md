## Text-to-Voice Conversion

`Psyflow` supports **text-to-speech (TTS)** conversion to enhance accessibility and standardize instruction delivery across different languages. 

**Why it matters**: Using text-to-speech improves accessibility—especially for children, elderly individuals, or participants with low literacy. It ensures consistent voice delivery across different language versions and eliminates the need to record human voiceovers for each translation. Moreover, by using standardized synthetic voices, it reduces variability introduced by different experimenters, helping to maintain consistency across sessions and sites.

**How It Works**: `Psyflow` uses Microsoft's `edge-tts`, a cloud-based TTS API that converts text to audio (MP3). The generated voice files are stored in the `assets/` folder, automatically skipped if they already exist (unless `overwrite=True` is specified), and registered into the `StimBank` as new `Sound` stimuli ready for playback.

```{Note}
An internet connection is required for TTS generation. Offline tools exist but produce lower-quality audio.
```


### Convert Existing Text Stimuli to Voice

```python
from psyflow import StimBank
stim_bank = StimBank(config)
stim_bank.convert_to_voice(keys=["instruction_text", "good_bye"], 
voice="zh-CN-YunyangNeural")
```
This will create audio files like `instruction_text_voice.mp3` in `assets/`.
 The resulting voices will be registered as `instruction_text_voice`, `good_bye_voice` in `StimBank`.


>If you plan to use voice output, make sure to delete any previously generated audio files in the `assets/` folder before generating new ones. Additionally, choose a TTS voice that matches the language of the text to ensure natural and accurate pronunciation. By default, "zh-CN-XiaoxiaoNeural" is used.


---

### Add Voice from Custom Text

If you want to add an arbitrary line of text as a voice stimulus:

```python
stim_bank.add_voice(
    stim_label="welcome_voice",
    text="ようこそ。タスクを開始します。",
    voice="ja-JP-NanamiNeural"
)
```
The result will be registered as `welcome_voice` and available like any other stimulus.


### Voice Selection

Use the built-in helper to explore available voices:

```python
from psyflow.tts_utils import list_supported_voices

# Print all voices
list_supported_voices(human_readable=True)

# Print all Japanese voices
list_supported_voices(filter_lang="ja", human_readable=True)
```

Sample output:
| ShortName              | Locale | Gender | Personalities       | FriendlyName                                                                 |
|------------------------|--------|--------|----------------------|-------------------------------------------------------------------------------|
| af-ZA-AdriNeural       | af-ZA  | Female | Friendly, Positive   | Microsoft Adri Online (Natural) - Afrikaans (South Africa)                   |
| af-ZA-WillemNeural     | af-ZA  | Male   | Friendly, Positive   | Microsoft Willem Online (Natural) - Afrikaans (South Africa)                 |
| sq-AL-AnilaNeural      | sq-AL  | Female | Friendly, Positive   | Microsoft Anila Online (Natural) - Albanian (Albania)                        |
| sq-AL-IlirNeural       | sq-AL  | Male   | Friendly, Positive   | Microsoft Ilir Online (Natural) - Albanian (Albania)                         |

Alternatively, you can check the list of supported voices [here](https://gist.github.com/BettyJJ/17cbaa1de96235a7f5773b8690a20462).


### Tips and Caveats

- **Placeholder Limitation**: The TTS engine does **not** support dynamic text with placeholders such as `{duration}` or `{block_num}`. If your text includes placeholders, it will not be converted as expected — the synthesis may fail or result in unnatural output.

- **Internet Connection Required**: TTS generation relies on Microsoft’s cloud service and requires a stable internet connection. If you're offline or behind a restrictive network (e.g., with proxy issues), voice generation will fail.

- **Overwrite**: Use `overwrite=True` to regenerate voice files even if they exist. However, be careful with this option, as it assumes you need to regenerate the voice every time you run the task ⚠️.

- **Voice Mismatch**: Always match the voice language to the text language to avoid unnatural pronunciation. By default, "zh-CN-XiaoxiaoNeural" is used.

- **Preview Your Audio**: You can test output files manually in the `assets/` folder before running full experiments.  
  If a file is empty or not playable, it may cause the task to fail at runtime — try deleting and regenerating the voice file.





