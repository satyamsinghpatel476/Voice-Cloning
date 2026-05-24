# 🎙️ Multilingual Voice Cloning using XTTS v2


## 🎥 Project Demo

[![Watch Demo](https://img.youtube.com/vi/abc123XYZ/0.jpg)](https://youtu.be/R5fHnWuxh0A)

---


## 📌 Project Overview
This project implements a zero-shot voice cloning system capable of generating multilingual speech using a short speaker reference audio sample.

The system is built on top of Coqui TTS and utilizes the XTTS v2 model for high-quality speech synthesis.

The goal is to explore neural speech synthesis, speaker embedding consistency, and multilingual generalization.

---

## 🎯 Objective
- Build a voice cloning system using deep learning
- Support multilingual text-to-speech generation
- Maintain speaker identity across different languages
- Handle long-form text generation efficiently

---

## ⚡ How to Run

### 1. Clone Repository
```bash
git clone https://github.com/satyamsinghpatel476/Voice-Cloning.git
cd Voice-Cloning
```

### 2.  Install Dependencies
```bash
pip install TTS pydub numpy
```

### 3. Install FFmpeg
```bash
sudo apt install ffmpeg
```

Windows: Download and add FFmpeg to PATH

### 4. Run the Script
```bash
python main.py
```

### 5. Provide Inputs

Enter when prompted:

Audio:
enter audio file name :- sample  
enter audio format :- mp3  

Text:
Enter your text:- Hello this is a voice cloning test  

Language:
0: English, 1: Hindi, 2: Spanish, 3: French, 4: German, 5: Italian, 6: Portuguese, 7: Polish, 8: Turkish, 9: Russian, 10: Dutch, 11: Czech, 12: Arabic, 13: Chinese, 14: Japanese, 15: Korean  

Example:
enter language number :- 0

### 6. Output
Final generated file:
output.wav

```markdown
> 🎧 Best experienced with headphones for better audio quality
```

---

## 📁 Project Structure

main.py      → Main voice cloning script  
sample.mp3   → Example input audio  
output.wav   → Generated output  

---

## 🧠 System Architecture

The pipeline consists of the following stages:

1. Input speaker audio sample
2. Audio preprocessing (mono conversion, normalization, resampling)
3. Text segmentation into manageable chunks
4. XTTS v2 inference for speech synthesis
5. Post-processing (silence removal and smoothing)
6. Audio concatenation and final output generation

---

## 🌍 Supported Languages
The system supports 16 languages including:
English, Hindi, Spanish, French, German, Italian, Portuguese, Polish, Turkish, Russian, Dutch, Czech, Arabic, Chinese, Japanese, Korean

---

## 🧠 Key Features
- Zero-shot voice cloning from a single reference audio
- Multilingual speech synthesis capability
- Chunk-based long text processing
- Automatic silence trimming and normalization
- Consistent speaker embedding across segments

---

## 📊 Results
- Natural-sounding speech generated across multiple languages  
- High speaker similarity for short sentences  
- Acceptable intelligibility in cross-lingual synthesis  
- Stable output for moderate-length text inputs  

---

## 🧪 Experimental Analysis
- Speaker similarity remains high for short sequences  
- Slight degradation observed in long-form synthesis  
- Speaker embedding drift occurs across extended chunks  
- Cross-lingual quality depends on phonetic similarity with reference voice  
- Chunk-based processing improves stability but introduces boundary artifacts  

---

## 🔬 Technical Challenges Addressed
- Maintaining speaker consistency across long sequences
- Reducing artifacts in concatenated speech chunks
- Handling language-dependent pronunciation variation
- Ensuring stable synthesis for long-form text input

---

## 📊 Observations
- Speaker similarity remains high for short sentences
- Slight degradation observed in long-text synthesis
- Language transfer quality varies based on phonetic similarity to reference voice

---

## ⚙️ Limitations
- No explicit emotion control in speech output
- Speaker embedding drift in long sequences
- Dependent on quality of reference audio
- No real-time streaming implementation

---

## 🚀 Future Improvements
- Add emotion and style control (happy, sad, neutral)
- Improve speaker embedding stability for long text
- Build real-time web interface using Streamlit/Gradio
- Add voice similarity scoring metric
- Optimize inference speed for deployment

---

## 🧠 Key Learnings
- Neural TTS models can generalize across languages with shared embeddings
- Speaker identity preservation is a key challenge in long-form synthesis
- Chunk-based processing improves stability but introduces boundary artifacts
- Post-processing significantly improves perceived audio quality

---

## 🛠️ Tech Stack
- Python 3.8+
- Coqui TTS (XTTS v2)
- PyDub
- FFmpeg
- NumPy

---


## 🙋‍♂️ Author

**Satyam Singh Patel** 
[GitHub](https://github.com/satyamsinghpatel476)
