from pyscript import document
def compute_average(event):
            # Get input values
            score1 = document.getElementById("score1").value
            score2 = document.getElementById("score2").value
            
            # Check if inputs are provided
            if not score1 or not score2:
                document.getElementById("average").innerText = "Please enter both scores"
                document.getElementById("status").innerText = "Incomplete"
                return
            
            try:
                # Convert to numbers and calculate average
                num1 = float(score1)
                num2 = float(score2)
                avg = (num1 + num2) / 2
                
                # Display result
                document.getElementById("average").innerText = f"{avg:.2f}"
                
                # Determine pass/fail status
                if avg >= 75:
                    document.getElementById("status").innerText = "✅ Passed"
                    document.getElementById("status").className = "passed"
                else:
                    document.getElementById("status").innerText = "❌ Failed"
                    document.getElementById("status").className = "failed"
                    
            except ValueError:
                document.getElementById("average").innerText = "Invalid input"
                document.getElementById("status").innerText = "Error"
