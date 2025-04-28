import { Link } from "react-router-dom";
import { useState } from "react";
import { useAppContext } from "../context/AppContext";

function Sidebar() {
  const { testResults } = useAppContext();
  const [activeTab, setActiveTab] = useState("home");

  const handleTabClick = (tab) => {
    setActiveTab(tab);
  };

  return (
    <div>
      <div className="flex flex-col">
        {/* Home Tab */}
        <Link to="/introduction">
          <div
            onClick={() => handleTabClick("home")}
            className={`font-sans text-blue-300 text-xl flex justify-center items-center p-5 transition duration-300 no-underline ${
              activeTab === "home"
                ? "bg-[#121212] text-blue-400 shadow-[0_4px_2px_-1px_rgba(0,0,139,0.7)] transform "
                : "hover:bg-[#121212] hover:text-blue-400 hover:shadow-[0_4px_2px_-1px_rgba(0,0,139,0.7)]"
            }`}
          >
            <span>Home</span>
          </div>
        </Link>

        {/* Test My Project Tab */}
        <Link to="/upload-requirements">
          <div
            onClick={() => handleTabClick("test")}
            className={`font-sans text-blue-300 text-xl flex justify-center items-center p-5 transition duration-300 no-underline ${
              activeTab === "test"
                ? "bg-[#121212] text-blue-400 shadow-[0_4px_2px_-1px_rgba(0,0,139,0.7)] transform "
                : "hover:bg-[#121212] hover:text-blue-400 hover:shadow-[0_4px_2px_-1px_rgba(0,0,139,0.7)]"
            }`}
          >
            <span>Test My Project</span>
          </div>
        </Link>

        {/* Generate Report Tab */}
        {testResults.length !== 0 && (
          <Link to="/view-report">
            <div
              onClick={() => handleTabClick("report")}
              className={`font-sans text-blue-300 text-xl flex justify-center items-center p-5 transition duration-300 no-underline ${
                activeTab === "report"
                  ? "bg-[#121212] text-blue-400 shadow-[0_4px_2px_-1px_rgba(0,0,139,0.7)] transform "
                  : "hover:bg-[#121212] hover:text-blue-400 hover:shadow-[0_4px_2px_-1px_rgba(0,0,139,0.7)]"
              }`}
            >
              <span>Generate Report</span>
            </div>
          </Link>
        )}
      </div>
    </div>
  );
}

export default Sidebar;
