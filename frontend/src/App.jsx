import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home";
import Introduction from "./components/Introduction";
import { AppProvider } from "./context/AppContext";
import UploadRequirements from "./components/UploadRequirements";

function App() {
  return (
    <>
      <AppProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Home />}>
              <Route path="/" element={<Introduction />}></Route>
              <Route path="/introduction" element={<Introduction />}></Route>
              <Route
                path="/upload-requirements"
                element={<UploadRequirements />}
              ></Route>
            </Route>
          </Routes>
        </BrowserRouter>
      </AppProvider>
    </>
  );
}

export default App;
