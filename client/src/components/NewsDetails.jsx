import React from "react";
import { useLocation, useNavigate } from "react-router-dom";

const NewsDetails = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { newsItem, summary } = location.state;

  return (
    <div
      className="newsB"
      style={{
        backgroundImage: `url(${newsItem.url_to_image})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        color: "#fff", 
        padding: "20px",
        height: "100vh", 
        filter: "brightness(90%)",
      }}
    >
      <div className="hihi">
        <i onClick={() => navigate("/")} className="fas fa-home"></i>
        <h2>{newsItem.title}</h2>
      </div>

      <div className="newsF" style={{ background: "rgba(0, 0, 0, 0.6)", padding: "20px", borderRadius: "10px" }}>
        {/* Removing inline img tag since background is already set */}
        <div className="talha">
          <h3>Summary</h3>
          <p className="bai">{summary}</p>
        </div>
      </div>

      <div className="downD" style={{ background: "rgba(0, 0, 0, 0.6)", padding: "10px", borderRadius: "10px" }}>
        <div className="newsDB">
          <h3>Source: {newsItem.source_name}</h3>
          <p>Author: {newsItem.author}</p>
        </div>
        <div>
          <p>
            Source:{" "}
            <a target="_blank" href={newsItem.url} style={{ color: "#ffffff" }}>
              {newsItem.url}
            </a>
          </p>
          <p>Published at: {newsItem.published_at.substring(0, 10)}</p>
        </div>
      </div>
    </div>
  );
};

export default NewsDetails;
