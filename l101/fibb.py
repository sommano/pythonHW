def Xbonacci(signature,n):
    l = len(signature)
    if n <= l:
        return signature[:n]
    output = signature[::]
    for _ in range(n-l):
      output.append(sum(output[-l:]))
    return output    