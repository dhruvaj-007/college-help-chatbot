"""Rule-based College Help Chatbot using if/elif/else conditions.

Run in a terminal with: python chatbot.py
The chatbot runs locally and does not use an AI API or internet connection.
"""


def get_response(user_input: str) -> str:
    """Return a reply based on keyword rules in the user's message."""
    message = user_input.lower().strip()

    if not message:
        return "Please type a question about college, such as admissions, courses, fees, or exams."
    elif message in {"hi", "hello", "hey", "good morning", "good afternoon", "good evening"} or message.startswith("hello ") or message.startswith("hi "):
        return ("Hello! Welcome to College Help Chatbot. I can answer general questions about "
                "admissions, courses, fees, timings, exams, attendance, library, scholarships, "
                "hostel, transport, and placements. What would you like to know?")
    elif "help" in message or "what can you do" in message or "options" in message:
        return ("I can help with: admissions, courses, fees, college timings, exams, attendance, "
                "library, scholarships, hostel, transport, placements, and college contact details. "
                "Ask a question using one of these topics.")
    elif "admission" in message or "apply" in message or "enrol" in message or "enroll" in message:
        return ("Admissions: Check your college's official website or contact the admission office for "
                "eligibility, application dates, required documents, and the admission form. Requirements "
                "can vary by course and academic year.")
    elif "course" in message or "courses" in message or "degree" in message or "program" in message or "branch" in message:
        return ("Courses: Colleges may offer programs in areas such as Engineering, Science, Commerce, "
                "Arts, and Management. Tell me your college name or check its official prospectus for "
                "the exact course list.")
    elif "fee" in message or "fees" in message or "tuition" in message or "payment" in message:
        return ("Fees: The amount depends on your course, category, and academic year. Please check the "
                "official fee circular or contact the accounts office. Ask for the fee structure, due dates, "
                "accepted payment methods, and receipt process.")
    elif "time" in message or "timing" in message or "hours" in message or "working hour" in message or "college open" in message:
        return ("College timings: Class and office timings vary by institution and day. Check the latest "
                "timetable or notice board, or contact the college office to confirm today's schedule.")
    elif "exam" in message or "examination" in message or "timetable" in message or "result" in message:
        return ("Exams and results: Please use your college's official examination portal or notice board "
                "for exam timetables, hall-ticket instructions, results, and rechecking dates. Confirm the "
                "course and semester before following a notice.")
    elif "attendance" in message or "absent" in message or "leave" in message:
        return ("Attendance: Check your student portal or ask your class teacher for your current attendance "
                "percentage and the minimum required by your college. Submit leave requests through the "
                "official process and keep any required supporting documents.")
    elif "library" in message or "book" in message or "borrow" in message or "return book" in message:
        return ("Library: Visit the college library or library portal to search for books, check borrowing "
                "limits, renew loans, and confirm opening hours. Return books by the due date to avoid any "
                "applicable late fine.")
    elif "scholarship" in message or "scholarships" in message or "financial aid" in message or "fee concession" in message:
        return ("Scholarships: Eligibility and deadlines depend on the scheme. Ask the college scholarship "
                "office and check the relevant official government or institution portal. Keep income, identity, "
                "academic, and bank documents ready only when the scheme requires them.")
    elif "hostel" in message or "accommodation" in message or "mess" in message:
        return ("Hostel: Contact the hostel warden or student affairs office for room availability, application "
                "dates, fees, rules, mess details, and the list of required documents.")
    elif "transport" in message or "bus" in message or "commute" in message:
        return ("Transport: Ask the transport office for available bus routes, stops, timings, passes, fees, and "
                "safety rules. Routes can change, so confirm the current schedule before travelling.")
    elif "placement" in message or "career" in message or "internship" in message or "job" in message:
        return ("Placements: Contact the placement or career services cell for company visits, eligibility rules, "
                "resume reviews, internships, and interview schedules. Keep your resume and academic details updated.")
    elif "contact" in message or "phone number" in message or "email" in message or "address" in message or "office" in message:
        return ("Contact: For accurate phone numbers, email addresses, and campus directions, use the Contact Us "
                "page on your college's official website or ask the main reception. This demo does not contain "
                "college-specific contact information.")
    elif "thank" in message or "thanks" in message:
        return "You're welcome! Feel free to ask another college-related question."
    elif message in {"bye", "goodbye", "exit", "quit", "stop"} or "see you" in message:
        return "Goodbye! Best wishes for your studies. Type 'exit' in the terminal to close the chatbot."
    else:
        return ("Sorry, I don't have a rule for that question yet. Try asking about admissions, courses, fees, "
                "timings, exams, attendance, library, scholarships, hostel, transport, placements, or contact details.")


def main() -> None:
    """Run an interactive terminal chat session."""
    print("=" * 58)
    print("             COLLEGE HELP CHATBOT")
    print("=" * 58)
    print("Bot: Hello! Ask me about college services. Type 'help' for topics or 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Best wishes for your studies.")
            break

        if user_input.lower().strip() in {"exit", "quit", "stop"}:
            print("Bot: Goodbye! Best wishes for your studies.")
            break

        print("Bot:", get_response(user_input), "\n")


if __name__ == "__main__":
    main()
