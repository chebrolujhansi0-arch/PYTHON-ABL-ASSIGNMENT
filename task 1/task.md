
# Problem Statement
Develop a Python program to allocate university scholarships based on students’ aggregate marks, subject-wise minimum marks, attendance percentage, and family income. The program should identify eligible students, rank them according to their aggregate marks, and resolve ties using predefined rules.
# Assumptions
1. Students must score at least 75% aggregate marks.
2. Each subject must have a minimum of 60 marks out of 100.
3. Attendance must be at least 75%.
4. Annual family income must not exceed ₹2,50,000.
5. Eligible students are ranked by aggregate marks in descending order.
6. If aggregate marks are equal, higher attendance gets priority. If attendance is also equal, lower family income gets priority.
7. The program displays eligible students in rank order.
# Algorithm
1. Start the program.
2. Enter the number of students.
3. Input each student's name, subject marks, attendance, and annual family income.
4. Calculate aggregate marks as a percentage.
5. Check all scholarship eligibility conditions.
6. Store eligible students in a list.
7. Sort eligible students by aggregate marks, attendance, and family income using the predefined tie-breaking rules.
8. Display the eligible students with their ranks.
9. Stop the program.
# Mermaid Flowchart
```mermaid

#chatgpt-mermaid-_r_9g_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_9g_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_9g_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_9g_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-_r_9g_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-_r_9g_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_9g_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_9g_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_9g_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_9g_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_9g_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_9g_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_9g_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_9g_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-_r_9g_ p{margin:0;}#chatgpt-mermaid-_r_9g_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_9g_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_9g_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_9g_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_9g_ .label text,#chatgpt-mermaid-_r_9g_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_9g_ .node rect,#chatgpt-mermaid-_r_9g_ .node circle,#chatgpt-mermaid-_r_9g_ .node ellipse,#chatgpt-mermaid-_r_9g_ .node polygon,#chatgpt-mermaid-_r_9g_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-_r_9g_ .rough-node .label text,#chatgpt-mermaid-_r_9g_ .node .label text,#chatgpt-mermaid-_r_9g_ .image-shape .label,#chatgpt-mermaid-_r_9g_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_9g_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_9g_ .rough-node .label,#chatgpt-mermaid-_r_9g_ .node .label,#chatgpt-mermaid-_r_9g_ .image-shape .label,#chatgpt-mermaid-_r_9g_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_9g_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_9g_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_9g_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-_r_9g_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-_r_9g_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-_r_9g_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-_r_9g_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-_r_9g_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-_r_9g_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-_r_9g_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_9g_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_9g_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_9g_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_9g_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_9g_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_9g_ .icon-shape,#chatgpt-mermaid-_r_9g_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-_r_9g_ .icon-shape p,#chatgpt-mermaid-_r_9g_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-_r_9g_ .icon-shape .label rect,#chatgpt-mermaid-_r_9g_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-_r_9g_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_9g_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_9g_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-_r_9g_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_9g_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_9g_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_9g_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_9g_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_9g_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_9g_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_9g_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_9g_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-_r_9g_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_9g_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_9g_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_9g_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_9g_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_9g_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_9g_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_9g_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-_r_9g_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-_r_9g_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_9g_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_9g_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-_r_9g_ .node rect,#chatgpt-mermaid-_r_9g_ .node circle,#chatgpt-mermaid-_r_9g_ .node ellipse,#chatgpt-mermaid-_r_9g_ .node polygon,#chatgpt-mermaid-_r_9g_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_9g_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_9g_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_9g_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_9g_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_9g_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of studentsEnter name, subject marks,attendance and incomeCalculate aggregatepercentageAll eligibility criteria satisfied?Add student to eligible listMark student as not eligibleMore students?Sort by aggregate, attendanceand incomeDisplay eligible students withranksStopYesNoYesNo

```


# Pseudocode
START

INPUT number_of_students
CREATE empty eligible_list

FOR each student:
    INPUT name
    INPUT marks in all subjects
    INPUT attendance
    INPUT annual_family_income

    CALCULATE aggregate_percentage

    IF aggregate_percentage >= 75 AND
       every subject mark >= 60 AND
       attendance >= 75 AND
       income <= 250000 THEN

        ADD student to eligible_list
    END IF
END FOR

SORT eligible_list BY:
    aggregate marks in descending order
    attendance in descending order
    family income in ascending order

DISPLAY ranked eligible students

STOP


# Python Source Code
students = []n = int(input("Enter number of students: "))for i in range(n):    print("\nStudent", i + 1)    name = input("Enter student name: ")    marks = []    for j in range(1, 6):        mark = int(input(f"Enter marks in subject {j}: "))        marks.append(mark)    attendance = float(input("Enter attendance percentage: "))    income = int(input("Enter annual family income: "))    aggregate = sum(marks) / len(marks)    if (aggregate >= 75 and min(marks) >= 60            and attendance >= 75 and income <= 250000):        students.append({            "name": name,            "aggregate": aggregate,            "attendance": attendance,            "income": income        })students.sort(key=lambda s: (    -s["aggregate"], -s["attendance"], s["income"]))print("\n--- SCHOLARSHIP ELIGIBLE STUDENTS ---")if students:    for rank, s in enumerate(students, start=1):        print(            rank, s["name"],            "| Aggregate:", round(s["aggregate"], 2),            "| Attendance:", s["attendance"],            "| Income:", s["income"]        )else:    print("No eligible students found.")



# Sample Output
For example, suppose four students apply. Their details are entered as follows.
Student	Subject marks (5 subjects)	Attendance	Annual income
Asha	80, 78, 85, 90, 82	90%	₹2,00,000
Ravi	80, 78, 85, 90, 82	90%	₹1,80,000
Priya	75, 72, 80, 78, 75	88%	₹2,20,000
Kiran	90, 55, 80, 85, 90	95%	₹1,50,000

The resulting output is:
--- SCHOLARSHIP ELIGIBLE STUDENTS ---
1 Ravi | Aggregate: 83.0 | Attendance: 90.0 | Income: 180000
2 Asha | Aggregate: 83.0 | Attendance: 90.0 | Income: 200000
3 Priya | Aggregate: 76.0 | Attendance: 88.0 | Income: 220000


Kiran is not eligible because one subject mark is below 60. Ravi ranks above Asha because both have equal aggregate marks and attendance, but Ravi has lower family income.

# Conclusion
The program evaluates scholarship applicants based on aggregate marks, subject-wise minimum marks, attendance, and family income. It ranks eligible students and resolves ties using attendance and family income criteria.
