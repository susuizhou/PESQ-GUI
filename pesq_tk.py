import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from pesq import pesq
import soundfile as sf

def choose_file(entry):
    filepath = filedialog.askopenfilename()
    entry.delete(0, tk.END)  # 清除现有内容
    entry.insert(0, filepath)  # 插入新选择的路径

def calculate_pesq():
    ref_path = entry_ref.get()
    deg_path = entry_deg.get()

    try:
        ref_audio, ref_rate = sf.read(ref_path)
        deg_audio, deg_rate = sf.read(deg_path)

        assert ref_rate == 8000 and deg_rate == 8000, "Both files must have 8000 Hz sample rate"

        score = pesq(ref_rate, ref_audio, deg_audio, 'nb')
        messagebox.showinfo("PESQ Score", f"PESQ score: {score}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# 创建主窗口
root = tk.Tk()
root.title("PESQ Evaluation")

# 创建并添加文本说明
text_info = (
    "PESQ（Perceptual Evaluation of Speech Quality）是一种评估语音质量的客观算法\n\n"
    "PESQ的评分标准如下：\n\n"
    "4.5：几乎无损，与原始语音几乎无可辨识的差异。\n"
    "4.0：优秀的语音质量，细微的质量损失可能不被普通听众注意到。\n"
    "3.5：良好的语音质量，质量损失可感知，但不影响语音的理解。\n"
    "3.0：可接受的语音质量，明显的质量损失，可能会影响到语音的理解。\n"
    "2.5以下：语音质量较差，明显的失真和噪声，严重影响语音的理解和通信效果。\n\n"
    "需要注意的是，PESQ并不能完全代替人耳的主观评价，在评价语音质量时，PESQ评分通常与主观听觉测试相结合使用。\n"
    "输入文件需为8K采样率，16bit采样深度，wav格式\n"
    "2024年2月22日15:03:12 by susz\n"
)
text_widget = scrolledtext.ScrolledText(root, height=15, width=80)
text_widget.insert(tk.INSERT, text_info)
text_widget.pack(padx=10, pady=10)
text_widget.configure(state='disabled')  # 禁止用户编辑文本

# 创建输入框，让用户输入或选择文件路径
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_ref = tk.Entry(frame, width=50)
entry_ref.pack(side=tk.LEFT, padx=(0, 5))
button_ref = tk.Button(frame, text="Choose Reference File", command=lambda: choose_file(entry_ref))
button_ref.pack(side=tk.LEFT)

frame = tk.Frame(root)
frame.pack(padx=10, pady=5)

entry_deg = tk.Entry(frame, width=50)
entry_deg.pack(side=tk.LEFT, padx=(0, 5))
button_deg = tk.Button(frame, text="Choose Degraded File", command=lambda: choose_file(entry_deg))
button_deg.pack(side=tk.LEFT)

# 创建按钮，执行 PESQ 计算
button_calc = tk.Button(root, text="Calculate PESQ", command=calculate_pesq)
button_calc.pack(pady=(5, 0))

root.mainloop()
