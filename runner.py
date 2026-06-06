import time
from applicate import energy_estimater as em
import tkinter as tk

t = time.localtime()
hour = t.tm_hour

age = 0
sleeptime = 0.0
waterin = 0.0
energy = 0

def energy_leveler():
    if age <= 5:
        val = em.babies(sleeptime, waterin, hour)
    elif 6 <= age < 13:
        val = em.children(sleeptime, waterin, hour)
    elif 13 <= age < 19:
        val = em.teens(sleeptime, waterin, hour)
    elif 19 <= age < 31:
        val = em.youngadults(sleeptime, waterin, hour)
    elif 31 <= age < 65:
        val = em.adults(sleeptime, waterin, hour)
    else:
        val = em.elders(sleeptime, waterin, hour)
    return val
def task_sorter(tasklist):
    rem = energy

    tasklist.sort(key=lambda x: em.select_difficulty(x))
    tasklist.reverse()

    doable = []
    notdoable = []

    for x in tasklist:
        cost = em.select_difficulty(x)
        if rem >= cost:
            rem -= cost
            doable.append(x.capitalize())
        else:
            if rem < cost:
                rem = cost
            rem -= cost
            notdoable.append(x.capitalize())

    out = []
    out.append(f" This uses {energy-rem}% of energy.")
    out.append(f"You will have {round(rem)}% of energy left.")
    out.append("You can do:")
    for x in doable:
        out.append(x)
    out.append("Rest before you do:")
    for x in notdoable:
        out.append(x)
    return "\n".join(out)
def tkinter_file():
    global age, sleeptime, waterin, energy
    root = tk.Tk()
    root.title("VitalSync Calcualtor")

    tk.Label(root, text="Use numbers not letter for these 3 inputs.").grid(row=0, column=0)
    tk.Label(root, text="Age (years)").grid(row=1, column=0)
    agebox = tk.Entry(root)
    agebox.grid(row=1, column=1)
    tk.Label(root, text="Sleep (hrs)").grid(row=2, column=0)
    sleepbox = tk.Entry(root)
    sleepbox.grid(row=2, column=1)
    tk.Label(root, text="Water (L)").grid(row=3, column=0)
    waterbox = tk.Entry(root)
    waterbox.grid(row=3, column=1)

    energysect = tk.Label(root, text="Energy:")
    energysect.grid(row=4, column=1, columnspan=2, pady=5)

    tk.Label(root, text="Tasks (one per line)").grid(row=5, column=0)
    tasks = tk.Text(root, width=40, height=10)
    tasks.grid(row=5, column=1)
    output = tk.Text(root, width=50, height=12)
    output.grid(row=8, column=0, columnspan=2, pady=10)

    def run_all():
        global age, sleeptime, waterin, energy
        
        if agebox.get().isdigit() == False:
            output.delete("1.0", tk.END)
            output.insert(tk.END, "Age must be a number.")
            return
        s = sleepbox.get()
        w = waterbox.get()
        if s.replace('.', '').isdigit() == False:
            output.delete("1.0", tk.END)
            output.insert(tk.END, "Sleep must be a number.")
            return
        if w.replace('.', '', 1).isdigit() == False:
            output.delete("1.0", tk.END)
            output.insert(tk.END, "Water must be a number.")
            return
        age = int(agebox.get())
        sleeptime = float(s)
        waterin = float(w)
        energy = energy_leveler()
        energysect.config(text="Energy: " + str(energy) + "%")

        findtasks = tasks.get("1.0", tk.END).strip()
        if findtasks == "":
            output.delete("1.0", tk.END)
            output.insert(tk.END, "Enter tasks first.")
            return

        tasklist = findtasks.split("\n")
        result = task_sorter(tasklist)
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)

    tk.Button(root, text="Run", command=run_all).grid(row=7, column=0, columnspan=2, pady=5)
    root.mainloop()

tkinter_file()