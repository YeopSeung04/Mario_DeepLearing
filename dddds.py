import os

rom_path = 'rom/Super Mario Bros. (World).nes'

if os.path.isfile(rom_path):
    print("ROM 파일이 존재합니다.")
else:
    print("ROM 파일을 찾을 수 없습니다.")
