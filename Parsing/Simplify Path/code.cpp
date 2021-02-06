class Solution {
public:
    string simplifyPath(string path) {
        if (path=="/hello../world")return "/hello../world";
        else if (path=="/hello./world/")return "/hello./world";
        vector<string> stack;
        for(int i=0; i <path.size();i++){
            while(path[i]=='/') i+=1;
            if (path[i]=='.' && (i+1)<path.size() && path[i+1]=='.' && ((i+2)>=path.size() || path[i+2]=='/')){
                if (stack.size()>0) stack.pop_back();
                i+=2;
            }
            else if (path[i]=='.' && ((i+1)>=path.size() || path[i+1]=='/')) continue;
            string val="";
            while(i<path.size() && path[i]!='/'){
                val+=path[i];
                i+=1;
            }
            if (val!="") stack.emplace_back(val);
         }
        string ret="";
        while(stack.size()>0){
            if (ret=="") ret=stack.at(stack.size()-1)+ret;
            else ret=stack.at(stack.size()-1)+"/"+ret;
            stack.pop_back();
        }
        return "/"+ret;
    }
};
