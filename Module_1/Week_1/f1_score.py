# creat function to calculate Precision, Recall and F1-score
def f1_score(tp, fp, fn):
    # Print out all inputs
    print("------------------------------------------------------")
    print(f"Inputs: TP = {tp}, FP = {fp}, FN = {fn}")

    # Check whether any input is not integer and print it out
    if type(tp).isinstance() is False:
        print("TP must be integer.")
        return None

    if type(fp).isinstance() is False:
        print("FP must be integer.")
        return None

    if type(fn).isinstance() is False:
        print("FN must be integer.")
        return None

    # Check whether any input equals to or is smaller than zero
    if tp > 0 and fp > 0 and fn > 0:
        # Calculate Precision, Recall and F1-score and print them out
        precision = tp / (tp+fp)
        recall = tp / (tp+fn)
        f1 = 2 * (precision * recall) / (precision + recall)
        print("Precision is", precision)
        print("Recall is", recall)
        print("F1-score is", f1)
    else:
        print("TP and FP and FN must be greater than zero.")
        return None


# Run test cases
f1_score(tp=2, fp=3, fn=4)
f1_score(tp='a', fp=3, fn=4)
f1_score(tp=2, fp='a', fn=4)
f1_score(tp=2, fp=3, fn='a')
f1_score(tp=2, fp=3, fn=0)
f1_score(tp=2.1, fp=3, fn=0)
