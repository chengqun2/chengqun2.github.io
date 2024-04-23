1. useState
  const [count, setCount] = useState(0);
  const increment = () => {
    setCount(count + 1);
  };
2. useEffect
  useEffect(()=>{
    document.title = `Clicked ${count} times!`
  },[count]) 