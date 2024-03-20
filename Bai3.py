from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.btnSort.set_event_handler('click', self.btnSort_click)
    # Any code you write here will run before the form opens.

  

def btnSort_click(self, **event_args):
        # Lấy dãy số nguyên từ TextBox và chuyển đổi thành list
        input_text = self.txtInput.text
        numbers = list(map(int, input_text.split()))

        # Áp dụng thuật toán Insertion Sort để sắp xếp list
        self.insertion_sort(numbers)

        # Hiển thị kết quả sắp xếp lên TextBox kết quả
        self.txtResult.text = ' '.join(map(str, numbers))

    # Thuật toán Insertion Sort
def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
