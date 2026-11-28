import { Route, Routes } from "react-router-dom";
import Maintenance from "./pages/Maintenance";

function App() {
  return (
    <Routes>
      <Route path="*" element={<Maintenance />} />
    </Routes>
  );
}

export default App;
