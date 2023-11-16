# MyHeyGen | [EN](./README_en.md)

一个平民版视频翻译工具，音频翻译，翻译校正，视频唇纹合成全流程解决方案

## 参考项目（感谢他们的优秀作品）

[HeyGenClone](https://github.com/BrasD99/HeyGenClone.git)、[TTS](https://github.com/coqui-ai/tts)、[Video-retalking](https://github.com/OpenTalker/video-retalking)

## 实现效果

- [【好家伙一下子学了英语、日语、法语、俄语、韩语5国外语，肾好，肾好！ | MyHeyGen效果演示】](https://www.bilibili.com/video/BV1wC4y1E78h/?share_source=copy_web&vd_source=453c36b4abef37acd389d4c01b149023)
- [【张三老师英文普法！英文区的网友有福啦】](https://www.bilibili.com/video/BV1XN41137Bv/?share_source=copy_web&vd_source=453c36b4abef37acd389d4c01b149023)
- [【MyHeyGen测试|这英的英语倍儿地道！】](https://www.bilibili.com/video/BV1vN4y1D7mo/?share_source=copy_web&vd_source=453c36b4abef37acd389d4c01b149023)

## 视频教程

[【MyHeyGen来了！！！】]( https://www.bilibili.com/video/BV14C4y1J7dY/?share_source=copy_web&vd_source=453c36b4abef37acd389d4c01b149023)

## 微氪方案

[【MyHeyGen教程|这样配置应该简单很多吧】](https://www.bilibili.com/video/BV1cN4y1D73X/?share_source=copy_web&vd_source=453c36b4abef37acd389d4c01b149023)
相当于一键包，不需要配环境，但是得微氪金

## 环境准备

1. 在[huggingface申请token](https://huggingface.co/),放在config.json的HF_TOKEN参数下
2. 在[百度翻译申请APPKey](https://fanyi-api.baidu.com/?fr=pcHeader)用于翻译字幕放在config.json的TS_APPID和TS_APPKEY参数下
3.
下载`weights` [drive](https://drive.google.com/file/d/1dYy24q_67TmVuv_PbChe2t1zpNYJci1J/view?usp=sharing) [夸克](https://pan.quark.cn/s/284713c6e873)
放在MyHeyGen目录下，下载`checkpoints` [drive](https://drive.google.com/drive/folders/18rhjMpxK8LVVxf7PI6XwOidt8Vouv_H0?usp=share_link) [夸克](https://pan.quark.cn/s/7f7d82d57a1f)
放在video-retalking目录下,从weights复制GFPGANv1.4.pth到checkpoints，如下图

<div>
  <figure>
  <img alt='weights文件目录' src="./img/weights.png?raw=true" width="300px"/>
  <img alt='checkpoints文件目录' src="./img/checkpoints.png?raw=true" width="300px"/>
  <figure>
</div>

## 安装

```
git clone https://github.com/AIFSH/MyHeyGen.git
cd MyHeyGen
bash install.sh
```

或者拉取docker镜像

```
docker pull registry.cn-beijing.aliyuncs.com/codewithgpu2/aifsh-myheygen:o3U7yjrWg5
```

## 测试

```
python translate.py /root/MyHeyGen/test/src.mp4 'zh-cn' -o /root/MyHeyGen/test/out_zh.mp4
```

## 自己使用

```
python translate.py 原视频文件路径 想要翻译成的语言代码 -o 翻译好的视频路径
## 语言代码可以选择这些中之一：['en', 'es', 'fr', 'de', 'it', 'pt', 'pl', 'tr', 'ru', 'nl', 'cs', 'ar', 'zh-cn', 'ja','hu','ko']
##分别对应[英语、西班牙语、法语、德语、意大利语、葡萄牙语、波兰语、土耳其语、俄语、荷兰语、捷克语、阿拉伯语、中文（简体）、日语、匈牙利语、韩语]16种语言
```

## 适配 MacOS Arm

Macos M1pro 的版本上，修改以下这些关键依赖可以正常运行。

```
numpy==1.22.2
TTS==0.20.2
tensorflow==2.13.0
```

并且还有代码上的修改:

`MyHeyGen/core/voice_cloner.py`, line 7

```python
self.api = TTS(config["TTS_MODEL"], gpu=True)
```

`gpu=True` 修改为 `gpu=False`

## Update log

- 2023.11.16 update for macos arm
- 2023.11.7 add TTS_MODEL in config.json to custom model
- 2023.11.8 update TTS for more reality
- 2023.11.9 fix video-retalking oface error
- 2023.11.10 fix librosa version conflict with latest TTS

## 交流群及打赏码
<div>
  <figure>
  <img alt='交流群' src="./img/chat.jpg?raw=true" width="300px"/>
  <img alt='赏卤蛋' src="./img/ludan.jpg?raw=true" width="300px"/>
  <figure>
</div>
