; i dont like bubbles 

section .text
    global bubble
    default rel

bubble:
    push rbp
    mov  rbp, rsp
    push rbx

    mov  rbx, rdi        ; rbx = arr
    mov  ecx, esi        ; ecx = n
    dec  ecx             ; n - 1 outer loop count
    jle  .done

.outer:
    mov  edx, ecx        ; inner loop bound
    xor  eax, eax        ; i = 0

.inner:
    cmp  eax, edx
    jge  .next_outer

    ; load 8 elements
    vmovdqu ymm0, [rbx + rax*4]          
    vmovdqu ymm1, [rbx + rax*4 + 4]       

    ; arr[i] > arr[i+1]
    vpcmpgtd ymm2, ymm0, ymm1

    ; blend 
    vpblendvb ymm3, ymm0, ymm1, ymm2      
    vpblendvb ymm4, ymm1, ymm0, ymm2     

    vmovdqu [rbx + rax*4], ymm3
    vmovdqu [rbx + rax*4 + 4], ymm4

    add  eax, 8-1        
    jmp  .inner

.next_outer:
    dec  ecx
    jg   .outer

.done:
    pop  rbx
    pop  rbp
    vzeroupper
    ret
