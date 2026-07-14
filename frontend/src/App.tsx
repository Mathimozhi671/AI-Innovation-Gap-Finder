import Navbar from "./components/Navbar";
import SearchBox from "./components/SearchBox";

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <div className="max-w-7xl mx-auto p-8">

        <SearchBox />

      </div>
    </div>
  );
}

export default App;