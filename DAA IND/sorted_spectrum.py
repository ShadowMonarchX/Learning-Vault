import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import time


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")

        self.root.geometry("750x650")
        self.root.configure(bg="#2C3E50")

        self.canvas = tk.Canvas(root, width=700, height=300, bg="#ECF0F1", highlightthickness=2, highlightbackground="#34495E")
        self.canvas.pack(pady=20)

        ttk.Label(root, text="Select Sorting Algorithm:", background="#2C3E50", foreground="white", font=("Arial", 12, "bold")).pack(pady=5)

        self.algorithms = {
            "Bubble Sort": self.bubble_sort,
            "Selection Sort": self.selection_sort,
            "Insertion Sort": self.insertion_sort,
            "Quick Sort": lambda: self.quick_sort(0, len(self.data) - 1),
            "Merge Sort": lambda: self.merge_sort(0, len(self.data) - 1),
            "Heap Sort": self.heap_sort,
        }

        self.algorithm_dropdown = ttk.Combobox(root, values=list(self.algorithms.keys()), state="readonly", font=("Arial", 12))
        self.algorithm_dropdown.pack(pady=5)
        self.algorithm_dropdown.current(0)

        self.info_label = ttk.Label(root, text="Time: 0.000s  |  Comparisons: 0", background="#2C3E50", foreground="white", font=("Arial", 12, "bold"))
        self.info_label.pack(pady=5)

        ttk.Button(root, text="Start Sorting", command=self.start_sorting, style="TButton").pack(pady=10)
        ttk.Button(root, text="Generate New Array", command=self.generate_array, style="TButton").pack(pady=5)

        self.data = []
        self.comparisons = 0
        self.execution_time = 0  # Initialize execution_time here
        self.generate_array()

        
    def generate_array(self):
        self.data = np.random.randint(1, 100, 25).tolist()
        self.comparisons = 0
        self.draw_array(self.data)
    
    def draw_array(self, data, colors=None):
        self.canvas.delete("all")
        c_width = 700
        c_height = 300
        bar_width = c_width / len(data)
        max_height = max(data)
        
        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = c_height - (value / max_height) * (c_height - 20)
            x1 = (i + 1) * bar_width
            y1 = c_height
            color = "#E74C3C" if colors and colors[i] else "#3498DB"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="#34495E")
        self.info_label.config(text=f"Time: {self.execution_time:.5f}s  |  Comparisons: {self.comparisons}")

    def start_sorting(self):
        algorithm = self.algorithm_dropdown.get()
        self.execution_time = 0
        self.comparisons = 0
        start_time = time.time()
        self.algorithms[algorithm]()
        self.execution_time = time.time() - start_time
        self.draw_array(self.data)
    
    def bubble_sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(n - i - 1):
                self.comparisons += 1
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_array(self.data)
                    self.root.update()
                    time.sleep(0.05)
    
    def selection_sort(self):
        n = len(self.data)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.comparisons += 1
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.draw_array(self.data)
            self.root.update()
            time.sleep(0.05)
    
    def insertion_sort(self):
        n = len(self.data)
        for i in range(1, n):
            key = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j] > key:
                self.comparisons += 1
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
            self.draw_array(self.data)
            self.root.update()
            time.sleep(0.05)
    
    def quick_sort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quick_sort(low, pivot_index - 1)
            self.quick_sort(pivot_index + 1, high)
    
    def partition(self, low, high):
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            self.comparisons += 1
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        return i + 1
    
    def merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)
    
    def merge(self, left, mid, right):
        left_copy = self.data[left:mid + 1]
        right_copy = self.data[mid + 1:right + 1]
        l, r, sorted_idx = 0, 0, left
        while l < len(left_copy) and r < len(right_copy):
            self.comparisons += 1
            if left_copy[l] <= right_copy[r]:
                self.data[sorted_idx] = left_copy[l]
                l += 1
            else:
                self.data[sorted_idx] = right_copy[r]
                r += 1
            sorted_idx += 1
    
    def heap_sort(self):
        n = len(self.data)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heapify(i, 0)
    
    def heapify(self, n, i):
        largest, left, right = i, 2 * i + 1, 2 * i + 2
        if left < n and self.data[left] > self.data[largest]:
            largest = left
        if right < n and self.data[right] > self.data[largest]:
            largest = right
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(n, largest)

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()



# Here’s a breakdown of the **time complexity** and **space complexity** for each sorting algorithm you listed:

# ---

# ### 🔹 **Bubble Sort**
# - **Best Case (Already Sorted)**: \(O(n)\)
# - **Average Case**: \(O(n^2)\)
# - **Worst Case (Reversed Order)**: \(O(n^2)\)
# - **Space Complexity**: \(O(1)\) (In-place)

# ---

# ### 🔹 **Selection Sort**
# - **Best Case**: \(O(n^2)\)
# - **Average Case**: \(O(n^2)\)
# - **Worst Case**: \(O(n^2)\)
# - **Space Complexity**: \(O(1)\) (In-place)

# ---

# ### 🔹 **Insertion Sort**
# - **Best Case (Already Sorted)**: \(O(n)\)
# - **Average Case**: \(O(n^2)\)
# - **Worst Case (Reversed Order)**: \(O(n^2)\)
# - **Space Complexity**: \(O(1)\) (In-place)

# ---

# ### 🔹 **Quick Sort** (Lomuto Partitioning)
# - **Best Case**: \(O(n \log n)\)
# - **Average Case**: \(O(n \log n)\)
# - **Worst Case (Already Sorted, Unbalanced Partitions)**: \(O(n^2)\)  
#   _(Can be improved with randomized pivot selection)_
# - **Space Complexity**: \(O(\log n)\) (Average case due to recursive calls)

# ---

# ### 🔹 **Merge Sort**
# - **Best Case**: \(O(n \log n)\)
# - **Average Case**: \(O(n \log n)\)
# - **Worst Case**: \(O(n \log n)\)
# - **Space Complexity**: \(O(n)\) _(Extra space for merging)_

# ---

# ### 🔹 **Heap Sort**
# - **Best Case**: \(O(n \log n)\)
# - **Average Case**: \(O(n \log n)\)
# - **Worst Case**: \(O(n \log n)\)
# - **Space Complexity**: \(O(1)\) _(In-place, no extra storage needed)_

# ---

# ### ✅ **Summary Table**
# | Algorithm       | Best Case    | Average Case | Worst Case   | Space Complexity |
# |---------------|-------------|--------------|-------------|------------------|
# | Bubble Sort   | \(O(n)\)     | \(O(n^2)\)    | \(O(n^2)\)   | \(O(1)\)         |
# | Selection Sort| \(O(n^2)\)   | \(O(n^2)\)    | \(O(n^2)\)   | \(O(1)\)         |
# | Insertion Sort| \(O(n)\)     | \(O(n^2)\)    | \(O(n^2)\)   | \(O(1)\)         |
# | Quick Sort    | \(O(n \log n)\) | \(O(n \log n)\) | \(O(n^2)\) | \(O(\log n)\)    |
# | Merge Sort    | \(O(n \log n)\) | \(O(n \log n)\) | \(O(n \log n)\) | \(O(n)\) |
# | Heap Sort     | \(O(n \log n)\) | \(O(n \log n)\) | \(O(n \log n)\) | \(O(1)\) |

# ---

# ### 💡 **Which Sorting Algorithm to Choose?**
# - **If stability is important** → Use **Merge Sort or Insertion Sort**.
# - **If memory is a concern** → Use **Heap Sort or Quick Sort** (in-place sorting).
# - **For nearly sorted data** → Use **Insertion Sort** (\(O(n)\) in best case).
# - **For general-purpose sorting** → **Quick Sort** is often the fastest.

# Would you like a Python implementation for these algorithms? 🚀