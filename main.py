from pyscript import document

def compute_average(e):  
    score1 = float(document.getElementById("score1").value or 0)
    score2 = float(document.getElementById("score2").value or 0)

    avg = (score1 + score2) / 2

    if avg >= 75:
        message = f"Your average score is {avg:.2f} ✅ Passed"
    else:
        message = f"Your average score is {avg:.2f} ❌ Failed"

    document.getElementById("result").innerHTML = message

