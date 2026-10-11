# Voithos — FIZMAT IT Challenge 2023

> **Historical archive.** This repository is published as a time capsule, not as a maintained project. The code is preserved exactly as it was submitted to the competition.

---

## About This Project

**Voithos** is a multi-tool desktop application built with Python and Tkinter. It was created in the summer of 2023 for the **Fizmat IT Challenge** — a large-scale school-wide competition held at RFMSH (Republican Physics and Mathematics School, Kazakhstan) as part of the celebration of the school's 10th anniversary of innovation. The event brought together students from grades 1 through 10, who could compete individually or in teams across multiple tracks: Robotics, Game Development, Software, and FilmFest. Participants were judged on their engineering thinking, programming skills, and creative approach to solving real-world problems.

This project was submitted under the **Software** track, which focused on desktop and mobile applications built to serve a genuine purpose — ideally something useful to other students or people in everyday life.

The name **Voithos** (βοηθός) comes from ancient Greek and means *helper* or *assistant*. That was the core idea: a single desktop app that brings together several useful tools a student might actually reach for — playing music while studying, quickly looking something up on Wikipedia, translating a sentence, or experimenting with image processing. Rather than building one deep feature, the goal was to assemble a small toolkit that felt practical and personal.

The app launched as one of two versions developed during the competition period. `AITU_N1.py` was an earlier iteration focused on image filters, and `FIZMAT_IT_CHALLENGE.py` was the final submission that added OCR — the ability to extract text from any image using Tesseract. Both files are preserved here in their original state. The background images in the main menu were generated using the Dream by WOMBO neural network, which felt futuristic and fitting at the time.

Looking back, this was one of the first complete programs I ever finished and showed to real people. It wasn't polished. It had bugs. But it worked, and it was mine — and that mattered more than anything else at the time.

---

## What it does

The app is a single window that gives access to four tools via a navigation menu:

| Module | Description |
|---|---|
| **Audio Player** | Load and play `.mp3` files, skip tracks, pause/stop, control volume, and download audio from YouTube links |
| **Translator** | Translate text between languages using Google Translate — both with manual language codes and auto-detection |
| **Wikipedia Search** | Look up any topic on Wikipedia in any language, choosing the number of sentences to display |
| **Image Filters / OCR** | Apply filters (blur, contour, emboss, sharpen, edge enhance, custom RGB) to images, or extract text from images using Tesseract OCR |

---

## Tech stack

- **Python 3** — core language
- **Tkinter** — GUI framework
- **Pygame** — audio playback
- **Pillow** — image processing and filters
- **pytesseract** — OCR (text recognition from images)
- **googletrans** — translation API wrapper
- **wikipedia** — Wikipedia API wrapper
- **pytube** — YouTube video/audio downloader
- **moviepy** — video processing

---

## A note from the author

I'm uploading this in 2026, roughly three years after it was written. Back then I was just starting out — learning how to put libraries together, figuring out how event-driven GUIs work, and trying to build something that felt genuinely useful to other students at school.

The code is messy by any professional standard: global variables everywhere, no error handling, hardcoded paths, and a UI that was assembled more by trial-and-error than design. But that's exactly why I'm keeping it as-is. It's an honest record of where I was at the time — a snapshot of early curiosity before I knew the "right" way to do things.

If you're a student who just stumbled onto this: don't be discouraged by messy first projects. Everyone's early code looks like this. Ship it anyway, learn from it, and come back years later to see how far you've come.

---

## Running it (not recommended, but possible)

```bash
pip install pygame pillow pytesseract googletrans==4.0.0rc1 wikipedia pytube moviepy
```

You will also need [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and the path in `FIZMAT_IT_CHALLENGE.py` updated to match your system.

> Note: `pytube` and `googletrans` are known to break with newer Python/API versions. This code is not maintained and may not run out of the box.

---

*Submitted to Fizmat IT Challenge 2023 · RFMSH · Software track*


---

<sub>Account history: Magitcian172 → Eye172 (same developer). [Authorship note](AUTHORSHIP.md).</sub>
