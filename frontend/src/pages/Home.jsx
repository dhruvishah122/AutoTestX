import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

function Home() {
  return (
    <div className="h-screen w-screen  bg-[#121212] font-sans">
      <Navbar />

      {/* Container for Sidebar and View */}
      <div className="flex bg-[#121212] gap-4 h-155 flex-1  my-1   ">
        {/* Sidebar */}
        <div className="w-64  h-155 bg-black shadow-[0_2px_3px_-1px_rgba(0,0,255,0.7)] ">
          <Sidebar />
        </div>

        {/* View - Content Area */}
        <div className="flex-1 p-4 bg-[#121212] shadow-[0_2px_3px_-1px_rgba(0,0,255,0.7)] ">
          <Outlet />
        </div>
      </div>
    </div>
  );
}

export default Home;
