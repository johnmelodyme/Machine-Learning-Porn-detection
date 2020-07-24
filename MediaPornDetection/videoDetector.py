#!/usr/bin/env python
# 版權2020©John Melody Me
# 根據Apache許可版本2.0（“許可”）許可；
# 除非遵守許可，否則不得使用此文件。
# 您可以在以下位置獲得許可的副本：
# http://www.apache.org/licenses/LICENSE-2.0
# 除非適用法律要求或書面同意，否則軟件
# 根據許可分發的內容按“原樣”分發，
# 沒有任何明示或暗示的保證或條件。
# 有關特定語言的管理權限，請參閱許可證。
# 許可中的限制。
# @作者：John Melody Me
# http://www.scikit-video.org/stable/
import sys
import subprocess
import pkg_resources

# 檢查 "pillow" 和 "sightengine"" 是否已經安裝:
required_modules = {"pillow", "sightengine", "requests", "scikit-video"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required_modules - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
else:
    print("Dependencies Already Installed", required_modules, "\n")

import skvideo.io
import PIL
from PIL import Image
import numpy as np
import json
import os
import platform as p
import cv2
import time
# os.system("pip3 install sightengine")
from sightengine.client import SightengineClient

# 色情照片和視頻探測器:
class porn_video_detector:
    def main():
        # 我使用的是 SightengineApi(“用戶api”，“秘密api”）:
        client = SightengineClient('1069852127', 'tLNDZxAArCRND5p8qt7A')
        # 特別整數: 
        theSpecialInteger = 18
        # 獲取用戶輸入:
        dataLocation = input("Please input the data:  \n")
        # # 打開用戶輸入數據
        # __video = skvideo.io.vread(dataLocation)
        # # 使用 Numpy 將圖像轉換為數組
        # np__video = __video.shape
        # # 打印出數組的結果
        # print("Converted Video to Array " , np__video)
        # 聲明 SightengineApi 檢測功能
        output = client.check("nudity","wad","offensive","faces","face-attributes", "celebrities").video_sync(dataLocation)
        print(json.dumps(output, indent=4, sort_keys=True))
        time.sleep(2)
        # 將輸出和結果打印為 <<json>> 格式
        # 基於操作系統打開圖像或視頻
        computer_platform = p.system()
        if computer_platform == "Windows": 
            # __video.imopen()
            print("The Following Video is Explicit and inappropriate")
            cap = cv2.VideoCapture(dataLocation)
            # ret, frame = cap.read()
            while(1):
                ret, frame = cap.read()
                cv2.imshow("Video Data", frame)
                if cv2.waitKey(1) & 0xFF == ord("q") or ret == False:
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                cv2.imshow("Data", frame)
        elif computer_platform == "Darwin":
            # __video.imopen()
            os.system("say The Following Image is Explicit and inappropriate")
            print("The Following Video is Explicit and inappropriate")
            cap = cv2.VideoCapture(dataLocation)
            # ret, frame = cap.read()
            while(1):
                ret, frame = cap.read()
                cv2.imshow("Video Data", frame)
                if cv2.waitKey(1) & 0xFF == ord("q") or ret == False:
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                cv2.imshow("Data", frame)
        elif computer_platform == "Linux":
            # __video.imopen()
            os.system("mplayer The Following Image is Explicit and inappropriate")
            print("The Following video is Explicit and inappropriate")
            cap = cv2.VideoCapture(dataLocation)
            # ret, frame = cap.read()
            while(1):
                ret, frame = cap.read()
                cv2.imshow("Video Data", frame)
                if cv2.waitKey(1) & 0xFF == ord("q") or ret == False:
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                cv2.imshow("Data", frame)
        else:
            print("can't open image")

        

    if __name__ == "__main__":
        main()
        