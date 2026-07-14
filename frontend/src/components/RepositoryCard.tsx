interface Repository {
  name: string;
  description: string;
  stars: number;
  url: string;
}

interface Props {
  repo: Repository;
}

export default function RepositoryCard({ repo }: Props) {
  return (
    <div className="border rounded-lg shadow p-5">

      <h3 className="text-xl font-bold">
        {repo.name}
      </h3>

      <p className="mt-2">
        {repo.description}
      </p>

      <p className="mt-2">
        ⭐ {repo.stars}
      </p>

      <a
        href={repo.url}
        target="_blank"
        rel="noopener noreferrer"
        className="text-blue-600 font-semibold"
      >
        View Repository →
      </a>

    </div>
  );
}