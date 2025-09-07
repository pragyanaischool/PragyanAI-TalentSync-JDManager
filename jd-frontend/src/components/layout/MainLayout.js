import React from "react";
import Navbar from "./Navbar";

export default function MainLayout({ children }) {
  return (
    <div style={styles.container}>
      <Navbar />
      <main style={styles.mainContent}>{children}</main>
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    display: "flex",
    flexDirection: "column",
  },
  mainContent: {
    flex: 1,
    padding: "2rem",
    backgroundColor: "#f5f5f5",
  },
};
