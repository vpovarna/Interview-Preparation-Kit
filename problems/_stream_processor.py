from collections import defaultdict


class Problem:
    def __init__(self) -> None:
        self.dict = defaultdict(list[str])
    
    def process_stream(self, input: str):
        input_str = input.split(",")
        
        for word in input_str:
            current_str = word.strip()
            
            chars = list(current_str)
            chars.sort(reverse=True)
            
            key = "".join(set(chars))
            self.dict[key].append(current_str)
        
    def __str__(self) -> str:
        ans = ""
        for k,v in self.dict.items():
           ans = ans + f"{k} : {len(v)} {v}" + "\n"
        return ans


if __name__ == "__main__":
    problem = Problem()
    problem.process_stream("aab, cac, ac, ba, caa, d")
    
    print(problem)
