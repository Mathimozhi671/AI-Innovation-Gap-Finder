import { useState } from "react";
import axios from "axios";
import RepositoryCard from "./RepositoryCard";
import AnalysisCard from "./AnalysisCard";
import Loading from "./Loading";

interface Repository {
  name: string;
  description: string;
  stars: number;
  url: string;
}

interface ApiResponse {
  query: string;
  repositories: Repository[];
  ai_analysis: string;
}

export default function SearchBox() {
  const [query, setQuery] = useState("");
  const [repositories, setRepositories] = useState<Repository[]>([]);
  const [analysis, setAnalysis] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) {
      alert("Please enter a project idea.");
      return;
    }

    setLoading(true);

    try {
      const res = await axios.get<ApiResponse>(
        `http://127.0.0.1:8000/github/search`,
        {
          params: { query },
        }
      );

      setRepositories(res.data.repositories);
      setAnalysis(res.data.ai_analysis);
    } catch (error) {
      console.error(error);
      alert("Unable to connect to backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-5xl mx-auto mt-10">

      <div className="flex gap-3">

        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your AI project idea..."
          className="flex-1 border rounded-lg px-4 py-3"
        />

        <button
          onClick={handleSearch}
          className="bg-blue-600 text-white px-6 rounded-lg hover:bg-blue-700"
        >
          Search
        </button>

      </div>

      {loading && (
        <div className="mt-8">
          <Loading />
        </div>
      )}

      {!loading && repositories.length > 0 && (
        <>
          <h2 className="text-2xl font-bold mt-8 mb-4">
            GitHub Repositories
          </h2>

          <div className="grid gap-4">
            {repositories.map((repo) => (
              <RepositoryCard key={repo.url} repo={repo} />
            ))}
          </div>
        </>
      )}

      {!loading && analysis && (
        <>
          <h2 className="text-2xl font-bold mt-10 mb-4">
            AI Innovation Analysis
          </h2>

          <AnalysisCard analysis={analysis} />
        </>
      )}

    </div>
  );
}