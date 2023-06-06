# VoxExtract

VoxExtract is a Python project that allows you to download a YouTube video, extract the audio in .wav format, and separate the vocal track from the other sounds in the audio. It simplifies the process by reading the YouTube link and the save path from the "config.txt" file. All you need to do is run the "VoxExtract.py" script.

## Prerequisites

Before running VoxExtract, make sure you have the following requirements:

- Python 3.6 or higher
- FFmpeg installed on your system

## Installation

To get started with VoxExtract, follow these steps:

1. Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/your-username/VoxExtract.git
   ```

2. Navigate to the project directory:

   ```bash
   cd VoxExtract
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

To configure VoxExtract, open the "config.txt" file located in the project directory and modify the following values:

- **youtube_link**: Provide the YouTube video link that you want to extract audio from.
- **save_path**: Specify the path where you want to save the extracted audio file.

Make sure to save the "config.txt" file after making the necessary changes.

## Usage

To use VoxExtract, follow these steps:

1. Ensure that the "config.txt" file contains the correct YouTube link and save path.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the "VoxExtract.py" script:

   ```bash
   python VoxExtract.py
   ```

4. VoxExtract will download the YouTube video, extract the audio, and separate the vocal track. The progress will be displayed in the terminal.

5. Once the process is complete, you will find the separated vocal track saved at the specified path in the "config.txt" file.

## License

The VoxExtract project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute the code as per the terms of the license.

## Acknowledgements

VoxExtract relies on the following open-source libraries:

- [pytube](https://github.com/pytube/pytube): For downloading YouTube videos.
- [librosa](https://librosa.org/): For audio processing and feature extraction.
- [spleeter](https://github.com/deezer/spleeter): For vocal separation.

We would like to express our gratitude to the developers of these libraries for their contributions.

## Contributions

Contributions to VoxExtract are welcome! If you have any ideas, suggestions, or bug reports, please feel free to open an issue or submit a pull request on the project's GitHub repository.

Let's make VoxExtract better together!

---

Please note that extracting the vocal track from audio can be a complex task and may not always produce perfect results. The quality of the separation depends on various factors such as the original audio recording and the complexity of the audio content.