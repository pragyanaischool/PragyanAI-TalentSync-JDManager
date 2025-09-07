import { useState, useCallback } from "react";
import * as jdApi from "../api/jdApi";

export function useJdApi() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const createFromUrl = useCallback(async (url) => {
    setLoading(true);
    setError(null);
    try {
      const result = await jdApi.createJDFromUrl(url);
      setLoading(false);
      return result;
    } catch (err) {
      setLoading(false);
      setError(err.message);
      throw err;
    }
  }, []);

  const createFromFile = useCallback(async (file) => {
    setLoading(true);
    setError(null);
    try {
      const result = await jdApi.createJDFromFile(file);
      setLoading(false);
      return result;
    } catch (err) {
      setLoading(false);
      setError(err.message);
      throw err;
    }
  }, []);

  const queryJDs = useCallback(async (query) => {
    setLoading(true);
    setError(null);
    try {
      const result = await jdApi.queryJDs(query);
      setLoading(false);
      return result;
    } catch (err) {
      setLoading(false);
      setError(err.message);
      throw err;
    }
  }, []);

  return { loading, error, createFromUrl, createFromFile, queryJDs };
}
