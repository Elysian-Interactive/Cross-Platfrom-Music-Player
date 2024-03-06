from mutagen.oggvorbis import OggVorbis

def extract_ogg_metadata(ogg_file):
    metadata = {}
    try:
        audio = OggVorbis(ogg_file)
        print(audio.info.length)
        for key, value in audio.items():
            if isinstance(value, list):
                metadata[key] = ", ".join(value)
            else:
                metadata[key] = value
    except Exception as e:
        print(f"Error: {e}")
    return metadata

# Replace 'your_audio_file.ogg' with the path to your OGG file
metadata = extract_ogg_metadata('jungle.ogg')

# Print the extracted metadata
for key, value in metadata.items():
    print(f"{key}: {value}")