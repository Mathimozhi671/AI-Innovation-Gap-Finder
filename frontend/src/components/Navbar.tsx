function Navbar() {
  return (
    <nav className="bg-white shadow-md">
      <div className="max-w-7xl mx-auto flex justify-between items-center px-8 py-4">
        <h1 className="text-2xl font-bold text-blue-600">
          AI Innovation Gap Finder
        </h1>

        <div className="space-x-6">
          <button className="text-gray-700 hover:text-blue-600">
            Home
          </button>

          <button className="text-gray-700 hover:text-blue-600">
            Dashboard
          </button>

          <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
            Login
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;