### My react learning record
F:\react\my-vite-project

### useState
const [count, setCount] = useState(0);
const increment = () => {
  setCount(count + 1);
};
### useEffect
useEffect(()=>{
  document.title = `Clicked ${count} times!`
},[count]) 