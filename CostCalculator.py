import tkinter as tk
from tkinter import ttk
import base64
import os

def create_icon():
    icon_data = b'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAABIPzb/R0A6/0Y/Ov9GQDr/R0A6/0hAOf9IQDj/Rz85/0U+Of9EPTj/Rj44/0lAOf9GPjj/Rj86/0Y/N/9GPTX/RDw2/0dAOf9KQTn/Rz83/0Q+Nv9GPTb/Rz82/0U+Nv9DOzX/Qjw2/0M9N/9DPDb/Qzw0/0I6Mv9BOTD/QDcv/0tANf9KQjv/S0M9/0xFP/9KQz7/SkM9/0tEPP9LQzv/SEE7/0hBPP9KQTz/SEA5/0lDO/9IQTv/RD45/0Y/N/9HQDb/Rz84/0lBO/9JQjz/SUI6/0lCOv9IQTn/SEE5/0lBOf9GPjb/RT43/0U+OP9FPzj/RD01/0E6Mv9BOjL/SUA3/0pCO/9LRD3/TUU+/05HQf9NRkD/S0U//0pEPf9NRT3/TUU+/0xEPv9LQz3/SEE6/0hCOv9DOjb/PC0u/z4uLf9DODL/Rj82/0hAOv9JQz7/SkM8/0lCPP9KQjv/S0M6/0pDOf9IQDj/Rj84/0U/OP9FQDj/Rj42/0I8Nf9KQTj/S0Q9/0tFP/9MRUD/T0dB/05HQP9PSEL/TUZB/0tFQP9ORT7/UEc//0xEPf9IQjv/Qzcz/zY1I/86Wif/Olwr/zQ4IP8/Liv/RTsz/0Y/N/9IQTz/SkQ//0tEPf9LRD3/SUM7/0xDOv9JQjv/RT84/0U/N/9GQDj/Qz03/01DOv9NRT7/TkZA/05IQv9NR0H/TUZA/09JQ/9QSUL/UElD/0xGQf9LRUD/TUY9/0c4Nf84Qyb/eKtz/7/exf+63cb/dq14/zpcKv83LiH/QjIt/0Q9M/9HQTv/SUQ//0tFPv9MRD3/TEQ8/0tDO/9JQjr/R0A4/0VAOP9DPjf/TUQ9/05HQP9QSEH/UElC/05IQ/9PSkT/UEpD/1FKQ/9RS0P/UUlC/0tGPv9HOTb/N0Ij/4G2hP/V3t//hqF8/5mqlP/p8///ueHJ/12VW/8zRSH/Oywm/0U5M/9HQDj/SUI8/0xFP/9MRT3/TUU8/01EPP9KQzr/R0A4/0M9Nv9ORj7/UElE/1FKRv9QSUP/UUpD/1FLRf9STEX/UEpD/09IQv9PSkH/TDw4/zlAI/93sXn/9f///8fLz/9Uikj/eJZw/77Iwv+wu7H/1+rp/5nPpf9JeT//Njcg/z8uK/9EOjL/RT85/0lEQP9MRkD/S0Q+/0pDPP9IQjr/RkA4/05GP/9PSUX/UkxG/1JMRv9UTEX/VEtF/1FLRf9RS0X/UUxD/01AO/84PCX/bqlw/+Lw8P+UrpD/j6uG/9LY3f/l5O7/aJBa/1OJOv/Gysz/2tzm/8jl1v92rXb/Oloq/zYuIf9AMi7/Qzw1/0ZBOv9MRkD/S0ZA/0lDPP9HQTn/UUhA/1BKQ/9STEX/VU9H/1VOSP9UTUf/UUpF/1FLRP9OQz//Ozsm/2KhZf/o/vf/5enz/2aVXv9rlV3/w8zF/6zCr/+rua3/wczG/5Wki/9Oh0D/rLWr//f///+34cT/YJhc/zNEIP86LCX/QTUv/0U/Nv9LRT//S0U+/0lDO/9TSkH/Vk9H/1VNR/9TTUf/V1FK/1dQSf9UT0j/UUdE/z45KP9fml7/6f/5/7K6sv+WrZL/0NLY/+3t+P+DnXb/Soo6/7i9tP/n7fP/qLan/4CceP+/ycH/v87H/7W7t//D1M3/l8ye/0R0Ov80NyD/PTEr/0hBOf9LRT//S0U//1ZNQv9VTkb/Vk9K/1ZQSv9VTkf/VVBI/1RLR/8/Oi3/WZJY/+D88/+vtK//WatU/1u+Xv9qnGP/sL+y/8nPzv/H0cz/pbOi/1GPQv+brZT/+////+Lq6v9yiWf/MWcP/5yzjv/3/v//yuvc/3Wzd/85RCf/SkA8/05IQf9LRT//VU1D/1dQR/9WUEr/VlBK/1ZRSv9VTUn/QDcs/1GJUP/U9eT/6/P7/5+xof9dlVf/Xbdd/2XLZv9csFv/daFw/8bSzv/Q2dj/kKmL/8LOxf/Q4Nb/aZFX/2GESP9Ufjn/rM6q/9Hc3v/Fy8v/4vX1/3WEcf9CNzP/T0pF/0pFQP9UTUb/VlBJ/1dRSv9XUUv/V05K/0M4Lv9LgUf/2P3q/6yqrP9VT0f/nqGg/72/wP+TpZD/X5ZW/2C+X/9jzmj/VqlS/4Kle//N0NH//////8DUv/8vcAz/cI5W/9Xr3//e6+7/d4Nr/1ZdOv/u/fz/lZiX/z83L/9NSEP/SkVA/1VORv9WUUv/V1JM/1hSTf9FPTP/TIJI/9X+5/+vra//RkA4/z0zK/9JPzX/l5mS/6qsqv+2urn/iKCF/1qaUv9hxmD/Yctj/1ikUf+FpX//vsTA/8LWwf/E5cr/4e3x/2ZtVf9scFf/rrut/8HKx/9SS0X/S0U//05IQv9KRD//UkxF/1NPSv9ZVU//TkZC/1F+T//W/+r/r6yw/0Y/Nv87MSj/b2tj/7y/wf+rrKn/trm5/56jnP+tr63/trq4/3+dd/9YoU//Zcth/5DSjv99sHv/k6yO/+Ho7f/s+vr/jZSF/8nRx//J0dD/TkhD/0hCPv9PSkX/TklD/0tHQ/9VTUb/VE5J/1ZQTP9PTkb/yeHW/6yur/8+NjD/PjUq/4+Pi/+4uLv/Zola/1OWRf9wiGT/srW0/7i9vP+fo5v/vb2//7a9uP9/nXf/fLd1/3HMaP+QxIr/eqRx/56umv//////v8fE/0xGQv9OSEL/UEtG/05JRf9OSkX/S0dD/1lRSf9YUkv/VE5J/1lUUv/f5eX/WFFI/0U7Mf+vsLD/p6qk/12NTv9uz2z/cdx2/2LLZf9Vlkr/fIxy/8TFyf+Jinr/i5F9/7y8vv+rva3/bJJe/4Wsdv9xnmb/sb+v/8bMzP9KRT//TUdC/1FMSP9TTUj/UU1I/09LR/9MSEX/WlJJ/1pTSv9ZU03/S0VA/5SWk/+amZH/sLWy/5CgiP9fo1T/eeJ//2XCZv9cmlT/XqBX/2XKZv9cwlz/W49S/256W/99gGf/qaul/5GPi//L0NX/j6KM/7jEt//T19n/UEpF/05KRv9RS0f/UktG/1ROSP9TTkn/UUxI/01IQ/9YUEb/WlNK/1pVTf9aVE3/Rj42/3d0b/+jqKD/Xa1W/4Dzjf9fqlr/eYdq/7y9v/+3urn/e4Fr/2WnXP9q2W7/aMRq/2iWXv/CycP/Z2Ja/z83L//j5+f/zdbW/09KRP9XT0n/VlBL/1NOSv9TTkr/UEtH/1FNSP9RTEf/TkpF/1hSSv9YU0z/WVRN/1xWTv9PR0D/dXNu/5+hn/9CRTH/Y35V/2VZS//Z2dr/pKaf/7a6tf+pqqf/vby8/1+ZUv9043v/THM5/56fmP94dW7/qq2p/7vBvv9MR0L/UUxH/1ZQSv9XUUv/WFJM/1VPSv9TTkr/UUxH/1BLRf9OSUX/XFRN/1pVT/9ZU07/WVRO/09IQv93d3P/oqik/0ExKv+Me3j/mJKL/6Snn/+nq6T/gX51/5GVjP+lpqP/i458/1trRv+flZX/qa2m/7C3sv+wtLL/SkVA/1JNR/9VT0n/VU9J/1VPSv9UUEv/V1FL/1dQS/9TTkr/UEpG/0tGQv9YU0z/WFJO/1pVUf9cWFP/TUVA/3h4dP+Ym5b/UUU6/6Gbkv+Oh37/u8C7/8PMyP9rZVr/JxoH/6mvp/+1t7L/nZWR/4SFf/+an5n/ioiC/0Q8Nv9RTUv/VlJP/1ZRS/9VT0r/VU9L/1VPSv9TTkj/VVBK/1ZRS/9TTUn/TklE/11YUf9bVlL/WVVS/11YUv9SS0X/cW9q/8XOy/+eoJr/koqA/5aOg/+trqj/oKKc/6mspv+Sj4b/srWu/6Wmnf92bmb/NSsl/6atqP99eXT/TEZC/1VRT/9TT07/VFFP/1dTT/9VUU3/VlBM/1hSS/9TTkn/U05J/1ZQSf9QS0X/XVhS/2BbVf9hXVf/XVhS/1FLRv9raWX/8vz6/2ZgWP9pXlL/raia/4eBdf+1urT/197c/6Ogmv+urqj/xcfC/3NrY/84LSX/s7ay/4eDfv9MSEP/WlVP/1dSTf9WUk3/VVJO/1dUUP9YU07/VVFL/1VRTP9UUEv/U05I/1BMRv9eWFL/XVlU/19bVf9gXFf/XVlW/1dTTv+Cgn3/wcrG/4+Mgv+Qh3j/paGV/5CIe/+goJj/tru2/9Te2v+IhHr/PDAk/6CinP/Ey8f/W1ZP/1RPTP9ZVFD/W1VQ/1tVT/9YU03/V1NP/1dTTv9ZVE//WVRO/1ZQS/9STUj/UEtF/15ZU/9eW1j/X1tY/2FcVv9gXFb/XltW/05JQ/9eWFL/h4aA/4WCdv+gm4r/mpOD/3dvZf+CeW//bmRY/0I3Kv/Axb//uLu2/1ZPSP9VUEr/WlVR/1ZSUP9YVFL/WFRQ/1pVT/9aVU7/WFRO/1dTTf9XUk3/WVNN/1ZQSv9PSkT/Yl1Y/2FeW/9gXVr/YF1Z/19cWP9fW1X/YFxX/1VRTf9VUk7/jIyG/2dkXP+GgXf/j4Z8/4mGfv+tr6r/yc7J/5iZlf9LRDz/WFRO/1lVUP9YU07/WlVS/1lVUv9XVFH/WlVQ/1tXUf9ZVU//WFNN/1ZSTf9UUEv/VE9K/1NOR/9gXFf/YmBe/2RiYP9iX13/YV5b/2FcV/9gW1X/X1tX/1dTTv9/fXX/fHdu/4iFff+Qi4L/q6+q/8/V0v92dG7/SkM8/1tWUf9bV1L/XFdR/1pWUf9bVlH/WlVQ/1tXU/9ZVVH/WVVQ/1dTT/9aVU//WFNO/1VRS/9TTkj/UEtG/2BcV/9hX1z/YWBe/2NhXv9iYF7/YV9b/2JeWf9hXVf/Yl1W/1pVT/93dW//eHRs/09JQf9bWFL/WlZR/1FMRv9eWlX/W1ZR/1tWUf9cV1L/XlpU/11ZVf9bVlL/WlVR/1tWUf9bV1P/WVVS/1dUUf9YVE//WFNN/1RPSf9QS0b/ZV9Z/2VhXf9hYF7/YWBe/2RjYP9nZGH/ZWNf/2NgXP9iX1r/Yl9a/1tXUv9ZVE7/YFtV/1lVT/9VUEz/WFRR/1pWUv9dWVT/XVlU/1tXUv9bWFT/XltW/15aVP9dWFP/WlVQ/1pWUf9aVlL/WFRS/1NRTv9VUUv/VFBK/1JNSP9lYFr/ZWNg/2RjYf9lZWP/ZmRi/2VjYf9lZGL/Z2Vh/2VjX/9iX1v/Y19b/2NhXf9hX1v/Yl5Z/2FdWP9fWlb/XVlU/1xZVP9eW1f/X1xY/1tXU/9aVlL/WldS/1xYUv9dWFD/W1VP/1lUUP9ZVE//VlJP/1RRTf9TT0v/UU5J/2dhWf9kY2D/Y2Jh/2RkZP9lZGT/ZmRi/2RiYP9kYmD/Z2Vg/2ZlYf9iYF7/Y19b/2RhXP9iX1v/YF5a/2JgXP9hXln/X1xX/1xZVv9cWlb/X1tW/1tWUf9ZVVL/V1VS/1lVUP9aVk//VlJN/1ZSTv9UUUz/VFFN/1NPS/9OS0b/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='
    with open("temp_icon.ico", "wb") as icon_file:
        icon_file.write(base64.b64decode(icon_data))

def calculate_cost(filament_grams, hours, device_power_watt, filament_cost_per_kg, electricity_cost_industrial, electricity_cost_home):
    device_power_kw = device_power_watt / 1000
    
    filament_cost = (filament_grams / 1000) * filament_cost_per_kg
    electricity_cost_industrial_total = device_power_kw * hours * electricity_cost_industrial
    electricity_cost_home_total = device_power_kw * hours * electricity_cost_home
    total_cost_industrial = filament_cost + electricity_cost_industrial_total
    total_cost_home = filament_cost + electricity_cost_home_total
    
    result_text.set(f"Filament Cost: €{filament_cost:.2f}\n"
                    f"Electricity Cost (Industrial): €{electricity_cost_industrial_total:.2f}\n"
                    f"Electricity Cost (Home): €{electricity_cost_home_total:.2f}\n"
                    f"Total Cost (Industrial): €{total_cost_industrial:.2f}\n"
                    f"Total Cost (Home): €{total_cost_home:.2f}")

def calculate_and_display():
    try:
        filament = float(entry_filament.get())
        hours = float(entry_hours.get())
        device_power_watt = float(entry_power.get())
        filament_cost_per_kg = float(entry_filament_cost.get())
        electricity_cost_industrial = float(entry_electricity_industrial.get())
        electricity_cost_home = float(entry_electricity_home.get())
        calculate_cost(filament, hours, device_power_watt, filament_cost_per_kg, electricity_cost_industrial, electricity_cost_home)
    except ValueError:
        result_text.set("Error: Please enter a valid number!")

# Main window
root = tk.Tk()
root.title("3D Printer Cost Calculator")
root.geometry("600x500")
root.configure(bg="#f0fff0")
create_icon()
root.iconbitmap("temp_icon.ico")

frame_main = tk.Frame(root, bg="#f0fff0")
frame_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

frame_left = tk.LabelFrame(frame_main, text="Input Data", bg="#f0fff0", font=("Arial", 12, "bold"), fg="#006400")
frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

frame_right = tk.LabelFrame(frame_main, text="Results", bg="#f0fff0", font=("Arial", 12, "bold"), fg="#006400")
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)

label_filament = ttk.Label(frame_left, text="Filament Used (grams):", background="#f0fff0", font=("Arial", 10))
label_filament.pack(pady=5)
entry_filament = ttk.Entry(frame_left, font=("Arial", 10))
entry_filament.pack(pady=5)

label_filament_cost = ttk.Label(frame_left, text="Filament Cost (€/kg):", background="#f0fff0", font=("Arial", 10))
label_filament_cost.pack(pady=5)
entry_filament_cost = ttk.Entry(frame_left, font=("Arial", 10))
entry_filament_cost.pack(pady=5)

label_hours = ttk.Label(frame_left, text="Usage Time (hours):", background="#f0fff0", font=("Arial", 10))
label_hours.pack(pady=5)
entry_hours = ttk.Entry(frame_left, font=("Arial", 10))
entry_hours.pack(pady=5)

label_power = ttk.Label(frame_left, text="Device Power (Watt):", background="#f0fff0", font=("Arial", 10))
label_power.pack(pady=5)
entry_power = ttk.Entry(frame_left, font=("Arial", 10))
entry_power.pack(pady=5)

label_electricity_industrial = ttk.Label(frame_left, text="Electricity Cost (€/kWh, Industrial):", background="#f0fff0", font=("Arial", 10))
label_electricity_industrial.pack(pady=5)
entry_electricity_industrial = ttk.Entry(frame_left, font=("Arial", 10))
entry_electricity_industrial.pack(pady=5)

label_electricity_home = ttk.Label(frame_left, text="Electricity Cost (€/kWh, Home):", background="#f0fff0", font=("Arial", 10))
label_electricity_home.pack(pady=5)
entry_electricity_home = ttk.Entry(frame_left, font=("Arial", 10))
entry_electricity_home.pack(pady=5)

button_calculate = ttk.Button(frame_left, text="Calculate", command=calculate_and_display)
button_calculate.pack(pady=10)

result_text = tk.StringVar()
label_result = ttk.Label(frame_right, textvariable=result_text, justify=tk.LEFT, anchor="w", padding=10, background="#f0fff0", font=("Arial", 10))
label_result.pack(fill=tk.BOTH, expand=True)

root.mainloop()

# Remove temporary icon file after application closes
if os.path.exists("temp_icon.ico"):
    os.remove("temp_icon.ico")
