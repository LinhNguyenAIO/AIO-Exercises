# Viết function thực hiện đánh giá classification model bằng F1-Score
import math

def calc_f1_score(tp, fp, fn):
  precision = tp/(tp+fp)
  recall = tp/(tp+fn)
  f1_score = 2*(precision*recall)/(precision+recall)
  return f1_score

def exercise1(tp, fp, fn):
  if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
    if not isinstance(tp, int):
      print('tp must be int')
    if not isinstance(fp, int):
      print('fp must be int')
    if not isinstance(fn, int):
      print('fn must be int')
    return
  if tp <= 0 or fp <= 0 or fn <= 0:
    print('tp and fp and fn must be greater than zero')
    return
  precision = tp / (tp + fp)
  recall = tp / (tp + fn)
  f1_score = 2 * (precision * recall) / (precision + recall)
  print(f'precision: {precision}')
  print(f'recall: {recall}')
  print(f'f1-Score: {f1_score}')

exercise1(tp=2, fp=3, fn=4)