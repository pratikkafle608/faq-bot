# Import necessary modules from Flask and Flask-CORS
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for all routes, allowing your React frontend to communicate with this backend.
# In a production environment, you would restrict this to your frontend's specific origin.
CORS(app)

# Define the knowledge base for the FAQ bot.
# This dictionary MUST be defined at the top-level of the file, outside of any function,
# so that it is accessible globally.
FAQ_ANSWERS = {
    # University Name
    "university name": "The name of the university is Texas A&M University-Texarkana.",
    "what is the name of the university": "The name of the university is Texas A&M University-Texarkana.",
    "school name": "The name of the university is Texas A&M University-Texarkana.",
    "full name of the institution": "The name of the university is Texas A&M University-Texarkana.",
    "tamut name": "The name of the university is Texas A&M University-Texarkana.",

    # University Location
    "where is it located": "Texas A&M University-Texarkana is located at 7101 University Avenue, Texarkana, Texas, 75503.",
    "university address": "Texas A&M University-Texarkana is located at 7101 University Avenue, Texarkana, Texas, 75503.",
    "school address": "Texas A&M University-Texarkana is located at 7101 University Avenue, Texarkana, Texas, 75503.",
    "campus location": "Texas A&M University-Texarkana is located at 7101 University Avenue, Texarkana, Texas, 75503.",
    "where is tamut": "Texas A&M University-Texarkana is located at 7101 University Avenue, Texarkana, Texas, 75503.",
    "address of texas a&m texarkana": "Texas A&M University-Texarkana is located at 7101 University Avenue, Texarkana, Texas, 75503.",

    # City Description (Texarkana)
    "what kind of city is texarkana": "Texarkana is a small city with a population of 36,193.",
    "how is texarkana": "Texarkana is a small city with a population of 36,193.",
    "texarkana population": "Texarkana is a small city with a population of 36,193.",
    "size of texarkana": "Texarkana is a small city with a population of 36,193.",
    "about texarkana city": "Texarkana is a small city with a population of 36,193.",

    # Student Count
    "total students": "2,109",
    "how many current students": "The total number of current students is 2,109.",
    "number of students": "The total number of current students is 2,109.",
    "current enrollment": "The total number of current students is 2,109.",
    "student population": "The total number of current students is 2,109.",
    "how many students attend tamut": "The total number of current students is 2,109.",

    # International Student Payment
    "pay tution":"International students usually prefer a wire transfer (also known as a swift transfer). The bank details are as follows: \n• Routing Transit Number: 121000248 \n• SWIFT/BIC code: WFBIUS6S \n• Bank name: Wells Fargo Bank, N.A. \n• Bank address: 420 Montgomery, San Francisco, CA 94104 \n• Beneficiary account name: Your name on your statement.",
    "How to pay tution": "International students usually prefer a wire transfer (also known as a swift transfer). The bank details are as follows: \n• Routing Transit Number: 121000248 \n• SWIFT/BIC code: WFBIUS6S \n• Bank name: Wells Fargo Bank, N.A. \n• Bank address: 420 Montgomery, San Francisco, CA 94104 \n• Beneficiary account name: Your name on your statement.",
    "How to pay tution?": "International students usually prefer a wire transfer (also known as a swift transfer). The bank details are as follows: \n• Routing Transit Number: 121000248 \n• SWIFT/BIC code: WFBIUS6S \n• Bank name: Wells Fargo Bank, N.A. \n• Bank address: 420 Montgomery, San Francisco, CA 94104 \n• Beneficiary account name: Your name on your statement.",
    "tution payment": "International students usually prefer a wire transfer (also known as a swift transfer). The bank details are as follows: \n• Routing Transit Number: 121000248 \n• SWIFT/BIC code: WFBIUS6S \n• Bank name: Wells Fargo Bank, N.A. \n• Bank address: 420 Montgomery, San Francisco, CA 94104 \n• Beneficiary account name: Your name on your statement.",
    "how to make payment as international students": "International students usually prefer a wire transfer (also known as a swift transfer). The bank details are as follows: \n• Routing Transit Number: 121000248 \n• SWIFT/BIC code: WFBIUS6S \n• Bank name: Wells Fargo Bank, N.A. \n• Bank address: 420 Montgomery, San Francisco, CA 94104 \n• Beneficiary account name: Your name on your statement.",
    "international student payment methods": "International students usually prefer a wire transfer (also known as a swift transfer). The bank details are as follows: \n• Routing Transit Number: 121000248 \n• SWIFT/BIC code: WFBIUS6S \n• Bank name: Wells Fargo Bank, N.A. \n• Bank address: 420 Montgomery, San Francisco, CA 94104 \n• Beneficiary account name: Your name on your statement.",
    "wire transfer details": "International students usually prefer a wire transfer (also known as a swift transfer). The bank details are as follows: \n• Routing Transit Number: 121000248 \n• SWIFT/BIC code: WFBIUS6S \n• Bank name: Wells Fargo Bank, N.A. \n• Bank address: 420 Montgomery, San Francisco, CA 94104 \n• Beneficiary account name: Your name on your statement.",
    "swift transfer information": "International students usually prefer a wire transfer (also known as a swift transfer). The bank details are as follows: \n• Routing Transit Number: 121000248 \n• SWIFT/BIC code: WFBIUS6S \n• Bank name: Wells Fargo Bank, N.A. \n• Bank address: 420 Montgomery, San Francisco, CA 94104 \n• Beneficiary account name: Your name on your statement.",
    "bank details for international payment": "International students usually prefer a wire transfer (also known as a swift transfer). The bank details are as follows: \n• Routing Transit Number: 121000248 \n• SWIFT/BIC code: WFBIUS6S \n• Bank name: Wells Fargo Bank, N.A. \n• Bank address: 420 Montgomery, San Francisco, CA 94104 \n• Beneficiary account name: Your name on your statement.",
    "how do international students pay tuition": "International students usually prefer a wire transfer (also known as a swift transfer). The bank details are as follows: \n• Routing Transit Number: 121000248 \n• SWIFT/BIC code: WFBIUS6S \n• Bank name: Wells Fargo Bank, N.A. \n• Bank address: 420 Montgomery, San Francisco, CA 94104 \n• Beneficiary account name: Your name on your statement.",

    # On-Campus Job Difficulty
    "how easy it is to get on-campus job": "Because it is a small campus, it is likely that you might be without a job for at least the first semester.",
    "on-campus job availability": "Because it is a small campus, it is likely that you might be without a job for at least the first semester.",
    "difficulty finding on-campus jobs": "Because it is a small campus, it is likely that you might be without a job for at least the first semester.",
    "is it hard to get an on-campus job": "Because it is a small campus, it is likely that you might be without a job for at least the first semester.",
    "chances of getting on-campus job": "Because it is a small campus, it is likely that you might be without a job for at least the first semester.",

    # How to Get a Job
    "how to get a job": "The best way to get a job is by making connections with faculty members.",
    "getting a job on campus": "The best way to get a job is by making connections with faculty members.",
    "job search tips": "The best way to get a job is by making connections with faculty members.",
    "finding employment": "The best way to get a job is by making connections with faculty members.",
    "advice for getting a job": "The best way to get a job is by making connections with faculty members.",

    # How to Apply for Jobs
    "how to apply for jobs": "To apply for jobs, submit a very refined and ATS-friendly resume. Also, submit as many recommendation letters as you can.",
    "job application process": "To apply for jobs, submit a very refined and ATS-friendly resume. Also, submit as many recommendation letters as you can.",
    "what do i need to apply for a job": "To apply for jobs, submit a very refined and ATS-friendly resume. Also, submit as many recommendation letters as you can.",
    "resume requirements for jobs": "To apply for jobs, submhow to ait a very refined and ATS-friendly resume. Also, submit as many recommendation letters as you can.",
    "recommendation letters for jobs": "To apply for jobs, submit a very refined and ATS-friendly resume. Also, submit as many recommendation letters as you can.",

    # International Student Scholarships
    "as an international student what are additional scholarships i can apply": "As an international student, you can apply for the Ambassador Program. You can also make connections with your professors to become an SI (Supplemental Instruction) leader. Additionally, you can apply to be a Resident Assistant in the dorm, which provides free housing and meals if you're approved.",
    "international student scholarships": "As an international student, you can apply for the Ambassador Program. You can also make connections with your professors to become an SI (Supplemental Instruction) leader. Additionally, you can apply to be a Resident Assistant in the dorm, which provides free housing and meals if you're approved.",
    "scholarship opportunities for international students": "As an international student, you can apply for the Ambassador Program. You can also make connections with your professors to become an SI (Supplemental Instruction) leader. Additionally, you can apply to be a Resident Assistant in the dorm, which provides free housing and meals if you're approved.",
    "ambassador program": "As an international student, you can apply for the Ambassador Program. You can also make connections with your professors to become an SI (Supplemental Instruction) leader. Additionally, you can apply to be a Resident Assistant in the dorm, which provides free housing and meals if you're approved.",
    "si leader position": "As an international student, you can apply for the Ambassador Program. You can also make connections with your professors to become an SI (Supplemental Instruction) leader. Additionally, you can apply to be a Resident Assistant in the dorm, which provides free housing and meals if you're approved.",
    "resident assistant benefits": "As an international student, you can apply for the Ambassador Program. You can also make connections with your professors to become an SI (Supplemental Instruction) leader. Additionally, you can apply to be a Resident Assistant in the dorm, which provides free housing and meals if you're approved.",

    # Off-Campus Housing
    "dorm": "As of now, you are required to stay in the dorm for your first year. However, if you're over 21 or have special housing needs, you can fill out a housing exemption form. If your application is approved based on your reasons, you can stay off-campus.",
    "housing": "As of now, you are required to stay in the dorm for your first year. However, if you're over 21 or have special housing needs, you can fill out a housing exemption form. If your application is approved based on your reasons, you can stay off-campus.",
    "off campus housing": "As of now, you are required to stay in the dorm for your first year. However, if you're over 21 or have special housing needs, you can fill out a housing exemption form. If your application is approved based on your reasons, you can stay off-campus.",
    "off-campus-housing": "As of now, you are required to stay in the dorm for your first year. However, if you're over 21 or have special housing needs, you can fill out a housing exemption form. If your application is approved based on your reasons, you can stay off-campus.",
    "can i live off-campus": "As of now, you are required to stay in the dorm for your first year. However, if you're over 21 or have special housing needs, you can fill out a housing exemption form. If your application is approved based on your reasons, you can stay off-campus.",
    "housing exemption form": "As of now, you are required to stay in the dorm for your first year. However, if you're over 21 or have special housing needs, you can fill out a housing exemption form. If your application is approved based on your reasons, you can stay off-campus.",
    "first year housing requirement": "As of now, you are required to stay in the dorm for your first year. However, if you're over 21 or have special housing needs, you can fill out a housing exemption form. If your application is approved based on your reasons, you can stay off-campus.",
    "dorms requirement": "As of now, you are required to stay in the dorm for your first year. However, if you're over 21 or have special housing needs, you can fill out a housing exemption form. If your application is approved based on your reasons, you can stay off-campus.",
    "housing for students over 21": "As of now, you are required to stay in the dorm for your first year. However, if you're over 21 or have special housing needs, you can fill out a housing exemption form. If your application is approved based on your reasons, you can stay off-campus.",

    #apartments for international students
    "apartment":"The apartment near texarkana that accepts tenants without income statments and credit history is Links and Bringle ridge",
    "popular apartment in texarkana":"The apartment near texarkana that accepts tenants without income statments and credit history is Links and Bringle ridge",
    "apartments in texarkana":"The apartment near texarkana that accepts tenants without income statments and credit history is Links and Bringle ridge",
    "what are some apartments in texarkana?":"The apartment near texarkana that accepts tenants without income statments and credit history is Links and Bringle ridge",
    "what are some apartments in texarkana":"The apartment near texarkana that accepts tenants without income statments and credit history is Links and Bringle ridge",
    "apartments around texarkana":"The apartment near texarkana that accepts tenants without income statments and credit history is Links and Bringle ridge",
    "apartments":"The apartment near texarkana that accepts tenants without income statments and credit history is Links and Bringle ridge",

    #tution for internation students
    "how much tution":"for fall it will be around $5,000, and for spring $6000 becuase insurance for fall is 1k and for spring is 2k since spring's insurance covers for spring as well as summer.",
    "tution":"for fall it will be around $5,000, and for spring $6000 becuase insurance for fall is 1k and for spring is 2k since spring's insurance covers for spring as well as summer.",
    "total tution":"for fall it will be around $5,000, and for spring $6000 becuase insurance for fall is 1k and for spring is 2k since spring's insurance covers for spring as well as summer.",
    "How much do i have to pay per semester": "for fall it will be around $5,000, and for spring $6000 becuase insurance for fall is 1k and for spring is 2k since spring's insurance covers for spring as well as summer.",
    "per semester tution":"for fall it will be around $5,000, and for spring $6000 becuase insurance for fall is 1k and for spring is 2k since spring's insurance covers for spring as well as summer.",

}   

# Define the API endpoint for the bot
@app.route('/ask', methods=['POST'])
def ask_bot():
    """
    Handles incoming POST requests to the /ask endpoint.
    Expects a JSON payload with a 'question' field.
    Returns a JSON response with the bot's answer.
    """
    try:
        # Get the JSON data from the request body
        data = request.get_json()

        if not data or 'question' not in data:
            # If no data or 'question' field is missing, return a 400 Bad Request error
            return jsonify({"error": "Invalid request: 'question' field is required."}), 400

        # Extract the question from the request and convert it to lowercase for matching
        user_question = data['question'].lower()
        print(f"Received question: {user_question}") # Log the received question for debugging

        # Find the best matching answer based on keywords
        # This is a simple approach; for more complex bots, consider NLP libraries like spaCy or NLTK
        bot_answer = "I'm sorry, I don't have an answer for that question. Please try rephrasing or ask about university name, location, student count, payments, jobs, or housing."
        for keyword, answer in FAQ_ANSWERS.items():
            if keyword in user_question:
                bot_answer = answer
                break # Found a match, so stop searching

        # Return the bot's answer as a JSON response
        return jsonify({"answer": bot_answer})

    except Exception as e:
        # Catch any unexpected errors and return a 500 Internal Server Error
        print(f"An error occurred: {e}") # Log the error for debugging
        return jsonify({"error": "An internal server error occurred."}), 500

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    # Run on host 0.0.0.0 to be accessible from other devices on the network (if needed)
    # and on port 5000 (default Flask port).
    # debug=True enables debug mode, which provides helpful error messages and auto-reloads the server
    # on code changes. Disable in production.
    app.run(host='0.0.0.0', port=5000, debug=True)
