model="WizardLM/WizardCoder-15B-V1.0"
temp=0.2
max_len=2048
pred_num=20
num_seqs_per_iter=1

output_path=preds/T${temp}_N${pred_num}

mkdir -p ${output_path}
echo 'Output path: '$output_path
echo 'Model to eval: '$model

num_problems=164

for i in $(seq 0 1 $((num_problems-1)))
do
    CUDA_VISIBLE_DEVICES=$gpu python humaneval_gen.py --model ${model} \
      --start_index ${start_index} --end_index ${end_index} --temperature ${temp} \
      --num_seqs_per_iter ${num_seqs_per_iter} --N ${pred_num} --max_len ${max_len} --output_path ${output_path};
done
