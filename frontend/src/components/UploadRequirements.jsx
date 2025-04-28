// import { useState, useEffect } from "react";
// import { useAppContext } from "../context/AppContext";
// import { AiOutlineFileText } from "react-icons/ai";
// import styles from "./UploadRequirements.module.css";

// function UploadRequirements() {
//   const {
//     fileName,
//     websiteURL,
//     loading,
//     testCases,
//     handleFileChange,
//     handleDragOver,
//     handleDrop,
//     handleURLChange,
//     handleGenerateTestCases,
//     handleRunTestCases, // New handler from context
//   } = useAppContext();

//   const [visibleTestCases, setVisibleTestCases] = useState([]);
//   const [loadingTestCaseIndex, setLoadingTestCaseIndex] = useState(0);
//   const [allTestCasesLoaded, setAllTestCasesLoaded] = useState(false); // NEW STATE

//   useEffect(() => {
//     if (testCases) {
//       setVisibleTestCases([]); // Reset when new testCases come
//       setLoadingTestCaseIndex(0); // Reset index
//       setAllTestCasesLoaded(false); // Reset loaded flag
//     }
//   }, [testCases]);

//   useEffect(() => {
//     if (testCases && loadingTestCaseIndex < testCases.length) {
//       const interval = setInterval(() => {
//         setVisibleTestCases((prev) => [
//           ...prev,
//           testCases[loadingTestCaseIndex],
//         ]);
//         setLoadingTestCaseIndex((prev) => prev + 1);
//       }, 300); // 0.3 second delay between each test case

//       return () => clearInterval(interval); // Cleanup
//     } else if (testCases && loadingTestCaseIndex === testCases.length) {
//       setAllTestCasesLoaded(true); // Set true once all testcases are shown
//     }
//   }, [testCases, loadingTestCaseIndex]);

//   return (
//     <div className="bg-[#121212] text-white my-5 px-4 flex h-130 justify-center">
//       <div className={styles.container}>
//         {!testCases && (
//           <div>
//             <h1 className={styles.heading}>Upload Your Requirements</h1>

//             {/* Drag and Drop Field */}
//             <div
//               className={styles.dragDropArea}
//               onDragOver={handleDragOver}
//               onDrop={handleDrop}
//             >
//               <input
//                 type="file"
//                 onChange={handleFileChange}
//                 className="hidden"
//                 id="fileUpload"
//               />
//               <label htmlFor="fileUpload" className={styles.dragDropLabel}>
//                 {fileName ? (
//                   <p className="text-green-400">{fileName}</p>
//                 ) : (
//                   <p>
//                     Drag & Drop your file here or{" "}
//                     <span className="underline text-blue-400 cursor-pointer">
//                       browse
//                     </span>
//                   </p>
//                 )}
//               </label>
//             </div>

//             {/* Website URL Field */}
//             <div className={styles.inputField}>
//               <input
//                 type="text"
//                 placeholder="Enter your project URL"
//                 value={websiteURL}
//                 onChange={handleURLChange}
//               />
//             </div>

//             {/* Generate Button */}
//             <button
//               onClick={handleGenerateTestCases}
//               className={styles.generateButton}
//               disabled={loading}
//             >
//               {loading ? "Generating...." : "Generate Test Cases"}
//             </button>
//           </div>
//         )}

//         {/* Display Test Cases */}
//         <div className={styles.testCaseContainer}>
//           {visibleTestCases.map((testCase, index) => (
//             <div className={styles.testCaseRow} key={index}>
//               <AiOutlineFileText className={styles.testCaseIcon} />
//               <p className={styles.testCaseDescription}>
//                 {testCase.description}
//               </p>
//             </div>
//           ))}
//         </div>

//         {/* Show Run Button only after ALL test cases are loaded */}
//         {allTestCasesLoaded && (
//           <button
//             onClick={handleRunTestCases}
//             className={`mt-5 ${styles.generateButton}`}
//           >
//             Run Test Cases
//           </button>
//         )}
//       </div>
//     </div>
//   );
// }

// export default UploadRequirements;

// import { useAppContext } from "../context/AppContext";
// import { AiOutlineFileText } from "react-icons/ai";
// import styles from "./UploadRequirements.module.css";

// function UploadRequirements() {
//   const {
//     fileName,
//     websiteURL,
//     loading,
//     testCases,
//     visibleTestCases,
//     allTestCasesLoaded,
//     handleFileChange,
//     handleDragOver,
//     handleDrop,
//     handleURLChange,
//     handleGenerateTestCases,
//     handleRunTestCases,
//   } = useAppContext();

//   return (
//     <div className="bg-[#121212] text-white my-5 px-4 flex h-130 justify-center">
//       <div className={styles.container}>
//         {!testCases && (
//           <div>
//             <h1 className={styles.heading}>Upload Your Requirements</h1>

//             {/* Drag and Drop Field */}
//             <div
//               className={styles.dragDropArea}
//               onDragOver={handleDragOver}
//               onDrop={handleDrop}
//             >
//               <input
//                 type="file"
//                 onChange={handleFileChange}
//                 className="hidden"
//                 id="fileUpload"
//               />
//               <label htmlFor="fileUpload" className={styles.dragDropLabel}>
//                 {fileName ? (
//                   <p className="text-green-400">{fileName}</p>
//                 ) : (
//                   <p>
//                     Drag & Drop your file here or{" "}
//                     <span className="underline text-blue-400 cursor-pointer">
//                       browse
//                     </span>
//                   </p>
//                 )}
//               </label>
//             </div>

//             {/* Website URL Field */}
//             <div className={styles.inputField}>
//               <input
//                 type="text"
//                 placeholder="Enter your project URL"
//                 value={websiteURL}
//                 onChange={handleURLChange}
//               />
//             </div>

//             {/* Generate Button */}
//             <button
//               onClick={handleGenerateTestCases}
//               className={styles.generateButton}
//               disabled={loading}
//             >
//               {loading ? "Generating...." : "Generate Test Cases"}
//             </button>
//           </div>
//         )}

//         {/* Display Test Cases */}
//         <div className={styles.testCaseContainer}>
//           {visibleTestCases.map((testCase, index) => (
//             <div className={styles.testCaseRow} key={index}>
//               <AiOutlineFileText className={styles.testCaseIcon} />
//               <p className={styles.testCaseDescription}>
//                 {testCase.description}
//               </p>
//             </div>
//           ))}
//         </div>

//         {/* Show Run Button only after ALL test cases are loaded */}
//         {allTestCasesLoaded && (
//           <button
//             onClick={handleRunTestCases}
//             className={`mt-5 ${styles.generateButton}`}
//           >
//             Run Test Cases
//           </button>
//         )}
//       </div>
//     </div>
//   );
// }

// export default UploadRequirements;

import { useAppContext } from "../context/AppContext";
import { AiOutlineFileText } from "react-icons/ai";
import styles from "./UploadRequirements.module.css";
import { FaRegSmileBeam } from "react-icons/fa";
import { FaCheckCircle, FaTimesCircle } from "react-icons/fa";

function UploadRequirements() {
  const {
    fileName,
    websiteURL,
    loading,
    testCases,
    visibleTestCases,
    allTestCasesLoaded,
    handleFileChange,
    handleDragOver,
    handleDrop,
    handleURLChange,
    handleGenerateTestCases,
    handleRunTestCases,
    testingInProgress,
    testResults,
  } = useAppContext();

  return (
    <div className="bg-[#121212] text-white my-5 px-4 flex h-130 justify-center">
      <div className={styles.container}>
        {/* Show waiting text if testingInProgress */}
        {testingInProgress && (
          <div className="flex flex-col items-center justify-center h-96">
            <p className="text-blue-400 text-2xl font-semibold animate-pulse">
              Hold tight! We are testing your project...
            </p>
          </div>
        )}

        {/* If there are test results, show them */}
        {!testingInProgress && testResults.length > 0 && (
          <div>
            <div className={`${styles.testCaseContainer} space-y-4`}>
              {testResults.map((result, index) => (
                <div
                  key={index}
                  className={`flex items-center gap-4 p-4 rounded-lg backdrop-blur-md bg-opacity-20
          ${result.result === "Passed" ? "bg-green-500/20" : "bg-red-500/20"}`}
                >
                  {result.result === "Passed" ? (
                    <FaCheckCircle className="text-green-400 text-3xl" />
                  ) : (
                    <FaTimesCircle className="text-red-400 text-3xl" />
                  )}
                  <p className="text-white text-left">{result.description}</p>
                </div>
              ))}
            </div>
            <div className="flex flex-col items-center justify-center mt-2 space-y-4">
              <p className="text-blue-300 text-xl font-semibold text-center">
                Testing complete! <br /> You can now view your detailed report.
              </p>
            </div>
          </div>
        )}

        {/* Otherwise, normal flow (Upload or Display Test Cases) */}
        {!testingInProgress && testResults.length === 0 && !testCases && (
          <div>
            <h1 className={styles.heading}>Upload Your Requirements</h1>

            {/* Drag and Drop Field */}
            <div
              className={styles.dragDropArea}
              onDragOver={handleDragOver}
              onDrop={handleDrop}
            >
              <input
                type="file"
                onChange={handleFileChange}
                className="hidden"
                id="fileUpload"
              />
              <label htmlFor="fileUpload" className={styles.dragDropLabel}>
                {fileName ? (
                  <p className="text-green-400">{fileName}</p>
                ) : (
                  <p>
                    Drag & Drop your file here or{" "}
                    <span className="underline text-blue-400 cursor-pointer">
                      browse
                    </span>
                  </p>
                )}
              </label>
            </div>

            {/* Website URL Field */}
            <div className={styles.inputField}>
              <input
                type="text"
                placeholder="Enter your project URL"
                value={websiteURL}
                onChange={handleURLChange}
              />
            </div>

            {/* Generate Button */}
            <button
              onClick={handleGenerateTestCases}
              className={styles.generateButton}
              disabled={loading}
            >
              {loading ? "Generating...." : "Generate Test Cases"}
            </button>
          </div>
        )}

        {/* Display Test Cases */}
        {!testingInProgress && testCases && (
          <div className={styles.testCaseContainer}>
            {visibleTestCases.map((testCase, index) => (
              <div className={styles.testCaseRow} key={index}>
                <AiOutlineFileText className={styles.testCaseIcon} />
                <p className={styles.testCaseDescription}>
                  {testCase.description}
                </p>
              </div>
            ))}
          </div>
        )}

        {/* Run Button */}
        {testResults.length === 0 &&
          !testingInProgress &&
          allTestCasesLoaded && (
            <button
              onClick={handleRunTestCases}
              className={`mt-5 ${styles.generateButton}`}
            >
              Run Test Cases
            </button>
          )}
      </div>
    </div>
  );
}

export default UploadRequirements;
