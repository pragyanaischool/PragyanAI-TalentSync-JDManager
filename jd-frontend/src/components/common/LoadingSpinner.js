import React from "react";

export default function LoadingSpinner() {
  return (
    <div style={{ textAlign: "center", padding: "1rem" }}>
      <div className="spinner" />
      <style jsx>{`
        .spinner {
          margin: auto;
          border: 4px solid #f3f3f3;
          border-top: 4px solid #0070f3;
          border-radius: 50%;
          width: 30px;
          height: 30px;
          animation: spin 1s linear infinite;
        }
        @keyframes spin {
          0%   { transform: rotate(0deg);}
          100% { transform: rotate(360deg);}
        }
      `}</style>
    </div>
  );
}
