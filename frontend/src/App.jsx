import { useState } from "react";
import { BrowserRouter as Router, Route,Routes } from "react-router-dom";
import Home from "./pages/Home";
function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" exact Component={Home} />
      </Routes>
    </Router>

  );
}

export default App;