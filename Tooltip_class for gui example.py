import tkinter as tk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
    
    def enter(self, event=None):
        if self.tooltip_window or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")  # Get widget size
        x += self.widget.winfo_rootx() + 25  # Offset x
        y += self.widget.winfo_rooty() + 20  # Offset y
        
        # Create a new Toplevel window
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)  # Remove window decorations
        self.tooltip_window.wm_geometry(f"+{x}+{y}")  # Position the tooltip
        
        label = tk.Label(self.tooltip_window, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
    
    def leave(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    button = tk.Button(root, text="Hover over me")
    button.pack(pady=50, padx=50)
    
    # Create a tooltip for the button
    Tooltip(button, "This is a tooltip text.")
    
    root.mainloop()
