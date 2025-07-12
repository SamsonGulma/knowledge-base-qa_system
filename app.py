import utils.session
from flask import Flask, request, render_template_string
from question_matching_engine import QuestionMatchingEngine


app = Flask(__name__)
qme = QuestionMatchingEngine()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Education QA System</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css">
</head>
<body class = "bg-gray-100">

<div class="bg-gray-100 text-white p-4 justify-center absolute right-0 bottom-10">
<ul class=" pl-1 font-light text-2xl text-black "> <p class = 'underline'> This Web-based Program is brought to you by: </p>
<li><span class="text-xl  p-2 font-light text-black "> Department of Software Engineering Students👨‍💻 </span></li>
<li><span class="text-xl  p-5 font-light text-black">1. Biruk Gebisa - UGR/25519/14</span></li>
<li><span class="text-xl  p-5 font-light text-black">2. Meron Bahiru - UGR/25880/14</span></li>
<li><span class="text-xl  p-5 font-light text-black">3. Samson Gulma - UGR/25654/14</span></li>
<li><span class="text-xl  p-5 font-light text-black">4. Tinsae Teferi - UGR/25753/14</span></li>

</ul>

</div>
<div class="bg-gray-100 flex items-center mt-40 justify-center"> 
<div class="w-full max-w-md p-6 bg-white rounded-lg shadow-lg">
        <h2 class="text-xl font-bold mb-4 text-center">👋 Hey there, How May I Assist you? </h2>

       <h2>❓ You can Ask me anything about Data Structure, Algorithms, Mathematics.</h2>


        <p class=" text-md font-light m-4 text-center">Please ask your question in this form. <br/> Eg. <span class = "text-red-600"> Tell me about [Subtopic] in [Main Topic].</span></p>
        <form action="/" method="POST" class="mb-4">
            <input type="text" name="question" placeholder="Enter your question..." 
                   class="w-full p-2 mb-4 border rounded-lg" required>
            <button type="submit" 
                    class="w-full bg-green-500 hover:bg-green-600 text-white py-2 rounded-lg">Get Answer</button>
        </form>
        {% if answer %}
            <div class="p-4 bg-green-100 rounded-lg">
                <strong>Answer:</strong>
                <p>{{ answer }}</p>
            </div>
        {% endif %}
        <p class="text-gray-600 m-4 text-center font-light text-sm">⚠️ Please Note that, I am fully relied on Knowledge Base, Not NLP</p> 
        
    </div>
</div>

    
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    if request.method == 'POST':
        question = request.form.get('question', '')
        answer = qme.get_answer(question)
    return render_template_string(HTML_TEMPLATE, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)