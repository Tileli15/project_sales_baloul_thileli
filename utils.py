import numpy as np

def generate_random_sales(min_val, max_val, size):
    # دالة ترجع مصفوفة أعداد صحيحة عشوائية بين القيم المطلوبة
    return np.random.randint(min_val, max_val + 1, size)
