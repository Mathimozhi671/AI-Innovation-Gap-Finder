interface Props {
  analysis: string;
}

export default function AnalysisCard({ analysis }: Props) {
  return (
    <div className="border rounded-lg shadow p-6 mt-5 whitespace-pre-wrap">
      {analysis}
    </div>
  );
}