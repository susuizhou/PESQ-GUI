# PESQ-GUI
PESQ-GUI

用于计算音频文件的评分，一个参考音频，一个带噪音频



PESQ（Perceptual Evaluation of Speech Quality）是一种评估语音质量的客观算法

PESQ的评分标准如下：

4.5：几乎无损，与原始语音几乎无可辨识的差异。
4.0：优秀的语音质量，细微的质量损失可能不被普通听众注意到。
3.5：良好的语音质量，质量损失可感知，但不影响语音的理解。
3.0：可接受的语音质量，明显的质量损失，可能会影响到语音的理解。
2.5以下：语音质量较差，明显的失真和噪声，严重影响语音的理解和通信效果。

需要注意的是，PESQ并不能完全代替人耳的主观评价，在评价语音质量时，PESQ评分通常与主观听觉测试相结合使用。
输入文件需为8K采样率，16bit采样深度，wav格式
2024年2月22日15:03:12 by susz



生成exe

pyinstaller --onefile --windowed pesq_src.py   支持文件拖入

pyinstaller --onefile --windowed pesq_tk.py