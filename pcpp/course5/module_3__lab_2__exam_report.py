import csv

with open('exam_results.csv', newline='') as exam_results_file:
    exam_results_reader = csv.DictReader(exam_results_file)

    exam_data = {}

    for exam_result in exam_results_reader:
        exam_name = exam_result['Exam Name']
        candidate_id = exam_result['Candidate ID']
        score = int(exam_result['Score'])
        grade = exam_result['Grade']
        passed_exam = grade == 'Pass'

        if exam_name not in exam_data:
            exam_data[exam_name] = {
                'candidates': {candidate_id},
                'passed': 0,
                'failed': 0,
                'best_score': score,
                'worst_score': score
            }

        exam = exam_data[exam_name]

        exam['candidates'].add(candidate_id)
        exam['passed'] += int(passed_exam)
        exam['failed'] += int(not passed_exam)
        exam['best_score'] = max(score, exam['best_score'])
        exam['worst_score'] = min(score, exam['worst_score'])

exam_report = [
    {
        "Exam Name": exam_name,
        "Number of Candidates": len(exam_metrics['candidates']),
        "Number of Passed Exams": exam_metrics['passed'],
        "Number of Failed Exams": exam_metrics['failed'],
        "Best Score": exam_metrics['best_score'],
        "Worst Score": exam_metrics['worst_score']
    }
    for exam_name, exam_metrics in exam_data.items()
]

with open('exam_report.csv', 'w', newline='') as exam_report_file:
    exam_report_writer = csv.DictWriter(exam_report_file, exam_report[0].keys())

    exam_report_writer.writeheader()
    exam_report_writer.writerows(exam_report)
