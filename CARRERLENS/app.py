print("==========================================")
print("              CAREERLENS")
print(" AI-Powered Employability & Career Analyzer")
print("==========================================")

# ---------------- USER INPUT ----------------

name = input("\nEnter Student Name: ")
role = input("Enter Target Job Role: ")

print("\n--- PROFILE INPUT ---")

resume = input("Resume available? (yes/no): ")
github = input("GitHub profile available? (yes/no): ")
portfolio = input("Portfolio available? (yes/no): ")
linkedin = input("LinkedIn profile available? (yes/no): ")


# ---------------- SKILLS ----------------

print("\n--- SKILL CLAIMS ----------------")
print("Enter: yes = Verified, weak = Weak, no = Unsupported")

java = input("Java skill evidence: ")
python = input("Python skill evidence: ")
sql = input("SQL skill evidence: ")
github_skill = input("GitHub skill evidence: ")


# ---------------- PROJECT EVIDENCE ----------------

print("\n--- PROJECT EVIDENCE ----------------")

projects = input("Project available? (yes/no): ")

if projects == "yes":
    project_quality = input(
        "Project quality (high/medium/low): "
    )

    project_depth = input(
        "Project depth (high/medium/low): "
    )
else:
    project_quality = "low"
    project_depth = "low"


# ---------------- ACTIVITY ----------------

print("\n--- CONSISTENCY OF ACTIVITY ----------------")

activity = input(
    "Activity over time (high/medium/low): "
)


# ---------------- CLAIM VERIFICATION ----------------

print("\n--- CLAIM-EVIDENCE VERIFICATION ---")

print("CareerLens compares each skill claim with available evidence.")

print("\nJava:")
if java == "yes":
    print("VERIFIED - Evidence supports Java skill")
elif java == "weak":
    print("WEAK - Limited Java evidence")
else:
    print("UNSUPPORTED - No Java evidence found")


print("\nPython:")
if python == "yes":
    print("VERIFIED - Evidence supports Python skill")
elif python == "weak":
    print("WEAK - Limited Python evidence")
else:
    print("UNSUPPORTED - No Python evidence found")


print("\nSQL:")
if sql == "yes":
    print("VERIFIED - Evidence supports SQL skill")
elif sql == "weak":
    print("WEAK - Limited SQL evidence")
else:
    print("UNSUPPORTED - No SQL evidence found")


print("\nGitHub:")
if github_skill == "yes":
    print("VERIFIED - GitHub evidence available")
elif github_skill == "weak":
    print("WEAK - Limited GitHub evidence")
else:
    print("UNSUPPORTED - No GitHub evidence found")


# ---------------- CLAIM-EVIDENCE MAP ----------------

print("\n==========================================")
print("          CLAIM-EVIDENCE MAP")
print("==========================================")

print("Java     -> Project Evidence ->", java)
print("Python   -> Project Evidence ->", python)
print("SQL      -> Project Evidence ->", sql)
print("GitHub   -> Repository Evidence ->", github_skill)


# ---------------- JOB READINESS SCORE ----------------
# PPT weights:
# Verified skill coverage = 40%
# Project quality & depth = 25%
# Consistency = 20%
# Portfolio & professional signals = 15%

print("\n==========================================")
print("        JOB READINESS SCORE")
print("==========================================")

# 40% - Verified Skill Coverage

verified_skills = 0

if java == "yes":
    verified_skills += 1

if python == "yes":
    verified_skills += 1

if sql == "yes":
    verified_skills += 1

if github_skill == "yes":
    verified_skills += 1

skill_score = (verified_skills / 4) * 40


# 25% - Project Quality and Depth

if project_quality == "high" and project_depth == "high":
    project_score = 25
elif project_quality == "high" or project_depth == "high":
    project_score = 20
elif project_quality == "medium" and project_depth == "medium":
    project_score = 15
elif projects == "yes":
    project_score = 10
else:
    project_score = 0


# 20% - Consistency

if activity == "high":
    consistency_score = 20
elif activity == "medium":
    consistency_score = 12
else:
    consistency_score = 5


# 15% - Portfolio and Professional Signals

signals = 0

if portfolio == "yes":
    signals += 1

if linkedin == "yes":
    signals += 1

if github == "yes":
    signals += 1

signal_score = (signals / 3) * 15


# FINAL SCORE

readiness_score = (
    skill_score
    + project_score
    + consistency_score
    + signal_score
)

print("Verified Skill Coverage :", round(skill_score, 2), "/ 40")
print("Project Quality & Depth  :", project_score, "/ 25")
print("Consistency Over Time    :", consistency_score, "/ 20")
print("Professional Signals     :", round(signal_score, 2), "/ 15")

print("------------------------------------------")
print("JOB READINESS SCORE:", round(readiness_score, 2), "/ 100")


# ---------------- ROLE FIT ----------------

print("\n==========================================")
print("             ROLE FIT")
print("==========================================")

print("Target Role:", role)

if readiness_score >= 75:
    print("Role Fit: STRONG")
elif readiness_score >= 50:
    print("Role Fit: MODERATE")
else:
    print("Role Fit: NEEDS IMPROVEMENT")


# ---------------- SKILL GAPS ----------------

print("\n==========================================")
print("             SKILL GAP REPORT")
print("==========================================")

gap_found = False

if java != "yes":
    print("- Java evidence needs improvement")
    gap_found = True

if python != "yes":
    print("- Python evidence needs improvement")
    gap_found = True

if sql != "yes":
    print("- SQL evidence needs improvement")
    gap_found = True

if github_skill != "yes":
    print("- GitHub/project evidence needs improvement")
    gap_found = True

if projects != "yes":
    print("- Build and document a project")
    gap_found = True

if not gap_found:
    print("No major skill gaps found.")


# ---------------- ROADMAP ----------------

print("\n==========================================")
print("        PERSONALIZED ROADMAP")
print("==========================================")

if java != "yes":
    print("1. Build one Java project and upload proof.")

if python != "yes":
    print("2. Build one Python project and document it.")

if sql != "yes":
    print("3. Practice SQL and create database project evidence.")

if github_skill != "yes":
    print("4. Upload projects and maintain GitHub activity.")

if project_quality != "high":
    print("5. Improve project quality and documentation.")

if activity != "high":
    print("6. Maintain consistent activity over time.")

if portfolio != "yes":
    print("7. Create a professional portfolio.")

if linkedin != "yes":
    print("8. Maintain a professional LinkedIn profile.")


# ---------------- REVIEWER VALIDATION ----------------

print("\n==========================================")
print("      CLAIM VERIFICATION VALIDATION")
print("==========================================")

print("For prototype validation, compare CareerLens")
print("result with a reviewer-labelled result.")

total_claims = 4
matched_claims = 0

print("\nEnter reviewer result for each claim.")
print("Use: yes / weak / no")

review_java = input("Reviewer - Java: ")
review_python = input("Reviewer - Python: ")
review_sql = input("Reviewer - SQL: ")
review_github = input("Reviewer - GitHub: ")


if java == review_java:
    matched_claims += 1

if python == review_python:
    matched_claims += 1

if sql == review_sql:
    matched_claims += 1

if github_skill == review_github:
    matched_claims += 1


accuracy = (matched_claims / total_claims) * 100

print("\nClaim Verification Accuracy:",
      round(accuracy, 2), "%")


# ---------------- LOW EVIDENCE WARNING ----------------

print("\n==========================================")
print("          EVIDENCE / RISK FLAG")
print("==========================================")

if github == "no" and portfolio == "no" and linkedin == "no":
    print("LOW EVIDENCE: More proof of work is required.")
else:
    print("Evidence sources are available.")


# ---------------- FINAL REPORT ----------------

print("\n==========================================")
print("          CAREERLENS FINAL REPORT")
print("==========================================")

print("Student:", name)
print("Target Role:", role)
print("Job Readiness:", round(readiness_score, 2), "/ 100")
print("Claim Verification Accuracy:",
      round(accuracy, 2), "%")

print("\nAnalysis completed successfully!")
print("CareerLens provides an explainable score,")
print("skill gaps and an improvement roadmap.")

print("==========================================")