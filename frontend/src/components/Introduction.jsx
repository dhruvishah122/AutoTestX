import styles from "./Introduction.module.css"; // Import the CSS module

function Introduction() {
  return (
    <div className={`bg-[#121212] text-white px-2 ${styles.fadeIn}`}>
      <div className="text-center mb-12 animate__animated animate__fadeIn">
        <h1 className="text-4xl font-extrabold text-blue-400 mb-4 animate__animated animate__fadeIn animate__delay-1s">
          Welcome to AutoTestX
        </h1>
        <p className="text-xl text-gray-300 mb-8 animate__animated animate__fadeIn animate__delay-2s">
          Revolutionizing project testing with intelligent, automated test case
          generation and execution.
        </p>
      </div>

      {/* Cards with Features in a Grid */}
      <div className={styles["grid-container"]}>
        {/* Effortless Testing */}
        <div className={`${styles.card} ${styles.fadeIn}`}>
          <h2>Effortless Testing</h2>
          <p>
            Just provide your project requirements, and let our tool do the
            heavy lifting for you.
          </p>
        </div>

        {/* Automated Process */}
        <div className={`${styles.card} ${styles.fadeIn}`}>
          <h2>Automated Process</h2>
          <p>
            Generate test cases based on your needs and let our system run them
            automatically.
          </p>
        </div>

        {/* Instant Results */}
        <div className={`${styles.card} ${styles.fadeIn}`}>
          <h2>Instant Results</h2>
          <p>
            Get detailed feedback and insights about your project after testing.
          </p>
        </div>

        {/* Generate Report */}
        <div className={`${styles.card} ${styles.fadeIn}`}>
          <h2>Generate Report</h2>
          <p>
            Easily generate comprehensive reports with actionable insights after
            every test.
          </p>
        </div>
      </div>
    </div>
  );
}

export default Introduction;
