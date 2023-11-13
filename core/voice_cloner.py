from TTS.api import TTS
from core.temp_manager import TempFileManager

class VoiceCloner:
    def __init__(self, config,lang_code):
        # self.api = TTS(f'tts_models/{lang_code}/fairseq/vits')
        self.api = TTS(config["TTS_MODEL"],gpu=True)
        self.lang_code = lang_code
        print("TTS model {} Loaded".format(config["TTS_MODEL"]))
    
    def process(self, speaker_wav_filename, text, out_filename=None):
        temp_manager = TempFileManager()
        if not out_filename:
            out_filename = temp_manager.create_temp_file(suffix='.wav').name
        self.api.tts_to_file(
            text,
            speaker_wav=speaker_wav_filename,
            file_path=out_filename,
            language=self.lang_code
        )
        return out_filename