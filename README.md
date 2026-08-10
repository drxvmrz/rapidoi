# ⚡ RAPIDOI

### ⏱️ One click to the article. One click to download. One DOI as filename

Researchers often download hundreds of PDFs: from open-access repositories, institutional proxies, or other sources. 
Manually typing or copy-pasting each DOI into a browser is so tedious. 
And then after downloading, files are named `main.pdf`, `document.pdf`, or worse. 
It's impossible to find them later or process these articles automatically.

### 🥷 RAPIDOI cuts through the chaos

**Open the article** -> one click on the DOI button.  
**Download the PDF** -> one click on the publisher's download button.  
**File is renamed** -> automatically to `<DOI NUMBER>.pdf`.

_That's it. Two clicks per article. No copy-pasting. No hunting for files._

### ⚠️ Disclaimer

RAPIDOI is a **file management and navigation tool**. It does not:
- Host, store, or distribute any copyrighted content;
- Bypass paywalls or authentication systems;
- Encourage or facilitate copyright infringement.

Users are responsible for ensuring their use of external sources (including custom resolvers) complies with local laws and the terms of service of those sources. 
The developers assume no liability for misuse of this tool.

# ⚖️ Features

- [x] **One-click article access** - no more typing URLs or copy-pasting DOIs
- [x] **Automatic file renaming** - downloaded PDFs become `DOI.pdf` instantly
- [x] **Customizable sources** - add any URL pattern for any DOI resolver (doi.org is available by default)
- [x] Completely standalone desktop app (Qt6-based GUI)
- [x] Configurable download folder (uses your operating system's **Downloads** folder by default)
- [x] Batch processing - load a list of DOIs and click through them in seconds

# 🧑‍🔬 System Requirements

> OS: Windows 10 or later, macOS 11 (Big Sur) or later, Linux/BSD distribution with Qt6 support

# ⚙️ Installation

Go to the [releases](https://github.com/drxvmrz/rapidoi/releases) and download the latest version of the installer. 
Then install it as usual on your operating system.

# 🧑‍🎓 Quick Start

1. Prepare a `.txt` file with a list of DOIs (see [example](https://github.com/drxvmrz/rapidoi/tree/main/_example_dois));
2. Open the file in RAPIDOI via the menu bar;
3. *(Optional)* Go to `Settings` -> `Sources` and add your preferred DOI resolver;
4. **Click the DOI** - the article page opens in your browser instantly;
5. *(Optional)* Go to `Settings` -> `Download path` and enter your default browser path to save downloads;
6. **Click "Download"** on the publisher's page - the PDF saves to your folder for downloaded files;
7. RAPIDOI **automatically renames** the file to `<DOI NUMBER>.pdf` - no manual renaming needed;
8. Repeat for the next DOI.

# 🧑‍💻 Build RAPIDOI by yourself

1. Download this repository;
2. Open the downloaded folder in the terminal or command prompt
   
   ```
   cd <PATH TO DOWNLOADED FOLDER>
   ```
3. Create a python virtual environment and activate it
   1. Windows
   ```
      python -m venv .venv ^
      .\.venv\Scripts\activate.bat
   ```
   2. Unix-like
   ```
      python -m venv venv \ 
      source venv/bin/activate
   ```
4. Install needed packages if missed
   ```
      pip install PySide6 nuitka platformdirs imageio
   ```
5. Run the Nuitka building
   1. Windows
   ```
      .\build_nuitka_win32.bat
   ```
   2. Unix-like
   ```
      chmod +x build_nuitka_mac.sh \
     ./build_nuitka_mac
   ```
6. Profit :)
