// import { createContext, useContext, useState } from "react";
// import axios from "axios";

// const AppContext = createContext();

// export const AppProvider = ({ children }) => {
//   const [fileName, setFileName] = useState("");
//   const [websiteURL, setWebsiteURL] = useState("");
//   const [testCases, setTestCases] = useState(null); // New state for fetched test cases
//   const [loading, setLoading] = useState(false);

//   const handleFileChange = (e) => {
//     const file = e.target.files[0];
//     if (file) {
//       setFileName(file.name);
//     }
//   };

//   const handleDragOver = (e) => {
//     e.preventDefault();
//   };

//   const handleDrop = (e) => {
//     e.preventDefault();
//     const file = e.dataTransfer.files[0];
//     if (file) {
//       setFileName(file.name);
//     }
//   };

//   const handleURLChange = (e) => {
//     setWebsiteURL(e.target.value);
//   };

//   const handleGenerateTestCases = async () => {
//     if (!fileName || !websiteURL) {
//       alert("Please upload a file and enter your website URL.");
//       return;
//     }

//     setLoading(true);

//     try {
//       // Fetching the test cases from the public directory
//       const response = await fetch("/test_cases.json");

//       if (!response.ok) {
//         throw new Error("Failed to fetch test cases.");
//       }

//       const receivedTestCases = await response.json();
//       setTestCases(receivedTestCases);

//       console.log(receivedTestCases);
//       // alert("Test cases generated successfully!");
//     } catch (error) {
//       console.error("Error:", error);
//       alert("Something went wrong while generating test cases.");
//     } finally {
//       setLoading(false);
//     }
//   };

//   const handleRunTestCases = () => {
//     console.log("Running test cases...");
//     // Add logic for running the test cases
//   };

//   return (
//     <AppContext.Provider
//       value={{
//         fileName,
//         websiteURL,
//         testCases,
//         loading,
//         handleFileChange,
//         handleDragOver,
//         handleDrop,
//         handleURLChange,
//         handleGenerateTestCases,
//         handleRunTestCases,
//       }}
//     >
//       {children}
//     </AppContext.Provider>
//   );
// };

// export const useAppContext = () => useContext(AppContext);

import { createContext, useContext, useState, useEffect } from "react";
import axios from "axios";

const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [fileName, setFileName] = useState("");
  const [websiteURL, setWebsiteURL] = useState("");
  const [testCases, setTestCases] = useState(null);
  const [visibleTestCases, setVisibleTestCases] = useState([]);
  const [loading, setLoading] = useState(false);
  const [loadingTestCaseIndex, setLoadingTestCaseIndex] = useState(0);
  const [allTestCasesLoaded, setAllTestCasesLoaded] = useState(false);
  const [testResults, setTestResults] = useState([]);
  const [testingInProgress, setTestingInProgress] = useState(false);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setFileName(file.name);
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if (file) {
      setFileName(file.name);
    }
  };

  const handleURLChange = (e) => {
    setWebsiteURL(e.target.value);
  };

  const handleGenerateTestCases = async () => {
    if (!fileName || !websiteURL) {
      alert("Please upload a file and enter your website URL.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("/test_cases.json");
      if (!response.ok) {
        throw new Error("Failed to fetch test cases.");
      }
      const receivedTestCases = await response.json();
      setTestCases(receivedTestCases);
    } catch (error) {
      console.error("Error:", error);
      alert("Something went wrong while generating test cases.");
    } finally {
      setLoading(false);
    }
  };

  const handleRunTestCases = async () => {
    setTestingInProgress(true);
    setTestCases(null); // Hide previous test cases
    setVisibleTestCases([]); // Also clear visible ones

    try {
      const response = await fetch("/test_results.json"); // assuming it’s in public folder
      const data = await response.json();
      setTestResults(data);
    } catch (error) {
      console.error("Failed to fetch test results:", error);
    } finally {
      setTestingInProgress(false);
    }
  };

  useEffect(() => {
    if (testCases) {
      setVisibleTestCases([]);
      setLoadingTestCaseIndex(0);
      setAllTestCasesLoaded(false);
    }
  }, [testCases]);

  useEffect(() => {
    if (testCases && loadingTestCaseIndex < testCases.length) {
      const interval = setInterval(() => {
        setVisibleTestCases((prev) => [
          ...prev,
          testCases[loadingTestCaseIndex],
        ]);
        setLoadingTestCaseIndex((prev) => prev + 1);
      }, 300);

      return () => clearInterval(interval);
    } else if (testCases && loadingTestCaseIndex === testCases.length) {
      setAllTestCasesLoaded(true);
    }
  }, [testCases, loadingTestCaseIndex]);

  return (
    <AppContext.Provider
      value={{
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
        testResults,
        testingInProgress,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => useContext(AppContext);
