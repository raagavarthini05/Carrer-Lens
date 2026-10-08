function analyzeProfile() {

    let name = document.getElementById("studentName").value;
    let role = document.getElementById("jobRole").value;

    let resume = document.getElementById("resume").value;
    let github = document.getElementById("github").value;
    let portfolio = document.getElementById("portfolio").value;
    let linkedin = document.getElementById("linkedin").value;

    let java = document.getElementById("java").value;
    let python = document.getElementById("python").value;
    let sql = document.getElementById("sql").value;

    let score = 0;

    // Profile evidence
    if (resume === "yes") {
        score += 15;
    }

    if (github === "yes") {
        score += 15;
    }

    if (portfolio === "yes") {
        score += 10;
    }

    if (linkedin === "yes") {
        score += 10;
    }

    // Skill evidence
    if (java === "verified") {
        score += 15;
    } else if (java === "weak") {
        score += 8;
    }

    if (python === "verified") {
        score += 15;
    } else if (python === "weak") {
        score += 8;
    }

    if (sql === "verified") {
        score += 10;
    } else if (sql === "weak") {
        score += 5;
    }

    let gaps = "";

    if (java !== "verified") {
        gaps += "• Improve Java project evidence<br>";
    }

    if (python !== "verified") {
        gaps += "• Improve Python project evidence<br>";
    }

    if (sql !== "verified") {
        gaps += "• Improve SQL project evidence<br>";
    }

    if (github === "no") {
        gaps += "• Add projects to GitHub<br>";
    }

    if (portfolio === "no") {
        gaps += "• Create a portfolio<br>";
    }

    if (linkedin === "no") {
        gaps += "• Complete LinkedIn profile<br>";
    }

    if (gaps === "") {
        gaps = "No major skill gaps found.";
    }

    let roadmap = "";

    if (score < 50) {
        roadmap =
            "1. Build practical projects<br>" +
            "2. Upload projects to GitHub<br>" +
            "3. Improve technical skills<br>" +
            "4. Create a professional portfolio";
    }
    else if (score < 75) {
        roadmap =
            "1. Strengthen weak skills<br>" +
            "2. Add more project evidence<br>" +
            "3. Improve portfolio and professional profile";
    }
    else {
        roadmap =
            "1. Continue building projects<br>" +
            "2. Improve project quality<br>" +
            "3. Prepare for interviews and placements";
    }

    document.getElementById("output").innerHTML =
        "<h3>Student: " + name + "</h3>" +
        "<p><b>Target Role:</b> " + role + "</p>" +
        "<h3>Job Readiness: " + score + " / 100</h3>" +

        "<h3>Skill Verification</h3>" +
        "<p>Java: " + java.toUpperCase() + "</p>" +
        "<p>Python: " + python.toUpperCase() + "</p>" +
        "<p>SQL: " + sql.toUpperCase() + "</p>" +

        "<h3>Skill Gaps</h3>" +
        "<p>" + gaps + "</p>" +

        "<h3>Improvement Roadmap</h3>" +
        "<p>" + roadmap + "</p>" +

        "<p><b>Analysis completed successfully!</b></p>";
}